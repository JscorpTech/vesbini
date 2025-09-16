from datetime import datetime

import httpx

from config.env import env
from core.apps.api.services.moysklad import active_retailshift


class MoySklad:
    def __init__(self) -> None:
        # INFO: base_uri https://api.moysklad.ru/api/remap/1.2
        self.base_uri = "https://api.moysklad.ru/api/remap/1.2"
        self.client = httpx.Client(
            base_url=self.base_uri,
            event_hooks={
                "request": [self.on_request],
            },
        )
        self.login = env.str("MOYSKLAD_LOGIN")
        self.password = env.str("MOYSKLAD_PASSWORD")
        self.org = "https://api.moysklad.ru/api/remap/1.2/entity/organization/0122d460-8198-11f0-0a80-03bb002d25d7"
        self.retailstore = (
            "https://api.moysklad.ru/api/remap/1.2/entity/retailstore/a3fd5441-0d84-11ed-0a80-026d001bdb75"
        )

    def on_request(self, request: httpx.Request):
        # request.headers["Accept-Encoding"] = "gzip"
        request.headers["Authorization"] = "Bearer {}".format(self.password)
        request.headers["Content-Type"] = "application/json"

    # ---------------------------------------
    # Pozitsiya yasash (product yoki bundle)
    # ---------------------------------------
    def product(self, quantity, amount, href, assortment_type: str = "product"):
        """
        product() endi universal:
        - assortment_type = "product" yoki "bundle"
        """
        return {
            "quantity": quantity,
            "price": amount,
            "assortment": {
                "meta": {
                    "href": href,
                    "type": assortment_type,
                }
            },
        }

    # ---------------------------------------
    # Store lar
    # ---------------------------------------
    def get_stores(self):
        res = self.client.get("entity/store")
        if res.status_code != 200:
            raise Exception("stores not found")
        return [
            {
                "href": row.get("meta", {}).get("href"),
                "name": row.get("name"),
            }
            for row in res.json().get("rows", [])
            if row.get("meta") and row.get("name")
        ]

    # ---------------------------------------
    # Product stock
    # ---------------------------------------
    def stok(self, codes=[], hrefs=[], kind: str = "product"):
        """
        kind = "product" (default) yoki "bundle"
        - product: mavjud stock qaytaradi
        - bundle: komponentlar variantlari asosida nechta bundle yig'ish mumkinligini hisoblaydi
        """
        if kind not in ("product", "bundle"):
            raise Exception("kind faqat 'product' yoki 'bundle' bo'lishi mumkin")

        if len(codes) == 0 and len(hrefs) == 0:
            raise Exception("codes yoki hrefs kiritish majburiy")

        if kind == "product":
            # PRODUCT STOCK
            if len(hrefs) <= 0:
                hrefs = self.products_href(codes)  # => (product_href, externalCode)
            url = ""
            for href, _ in hrefs:
                url += "product={};".format(href)
            response = self.client.get("report/stock/all?filter={}".format(url))
            rows = response.json().get("rows", [])
            if len(rows) <= 0:
                raise Exception("product not in stock")
            for row in rows:
                code = row.get("externalCode")
                quantity = row.get("quantity")
                yield code, quantity, row.get("meta", {}).get("href")
        else:
            # BUNDLE STOCK (komponent variantlari bo'yicha min floor hisob)
            if len(hrefs) <= 0:
                # hrefs => (bundle_href, externalCode, components_href)
                hrefs = list(self.bundles_href(codes))
            if len(hrefs) <= 0:
                raise Exception("Bundle topilmadi")
            for bundle_href, bundle_code, components_href in hrefs:
                components = self.bundle_components(components_href)  # [{variant_href, quantity}]
                possible_qty, _details = self.bundle_possible_quantity(components)
                yield bundle_code, possible_qty, bundle_href

    # ---------------------------------------
    # Product helperlar
    # ---------------------------------------
    def products_href(self, codes):
        """
        Product externalCode bo'yicha product meta hreflarini qaytaradi.
        return: generator (product_href, externalCode)
        """
        url = ""
        for code in codes:
            url += "externalCode={};".format(code)
        response = self.client.get(
            "entity/product/?filter={}".format(url),
        )
        rows = response.json().get("rows", [])
        if len(rows) <= 0:
            raise Exception("Product not found")
        for row in rows:
            yield row["meta"]["href"], row["externalCode"]

    # ---------------------------------------
    # Bundle helperlar
    # ---------------------------------------
    def bundles_href(self, codes):
        """
        Bundle externalCode bo'yicha bundle meta hreflari va components meta hrefini qaytaradi.
        return: generator (bundle_href, externalCode, components_meta_href)
        """
        url = ""
        for code in codes:
            url += "externalCode={};".format(code)
        response = self.client.get("entity/bundle/?filter={}".format(url))
        rows = response.json().get("rows", [])
        if len(rows) <= 0:
            raise Exception("Bundle not found")
        for row in rows:
            bundle_href = row["meta"]["href"]
            external_code = row.get("externalCode")
            components_meta_href = row.get("components", {}).get("meta", {}).get("href")
            if not components_meta_href:
                # Bundle komponentlari yo'q bo'lsa, 0 deb hisoblaymiz
                components_meta_href = ""
            yield bundle_href, external_code, components_meta_href

    def bundle_components(self, components_meta_href: str):
        """
        Bundle ichidagi komponentlarni qaytaradi.
        return: list of {variant_href: str, quantity: int}
        """
        if not components_meta_href:
            return []
        resp = self.client.get(components_meta_href)
        if resp.status_code != 200:
            raise Exception("Bundle components olinmadi")
        rows = resp.json().get("rows", [])
        components = []
        for row in rows:
            variant_href = row.get("assortment", {}).get("meta", {}).get("href")
            qty_required = row.get("quantity", 1)
            if variant_href:
                components.append({"variant_href": variant_href, "quantity": qty_required})
        return components

    def variant_stock(self, variant_href: str):
        """
        Variant stockini qaytaradi:
        return: {quantity: float|int, externalCode: str|None, href: str|None}
        """
        resp = self.client.get(f"report/stock/all/?filter=variant={variant_href}")
        rows = resp.json().get("rows", [])
        if not rows:
            return {"quantity": 0, "externalCode": None, "href": None}
        r0 = rows[0]
        return {
            "quantity": r0.get("quantity", 0),
            "externalCode": r0.get("externalCode"),
            "href": r0.get("meta", {}).get("href"),
        }

    def bundle_possible_quantity(self, components: list):
        """
        Komponentlar bo'yicha nechta bundle yig'ish mumkinligini hisoblaydi.
        components: [{variant_href, quantity}]
        return: (possible_bundle_qty: int, details: list)
        """
        if not components:
            return 0, []

        possible_counts = []
        details = []

        for comp in components:
            var_href = comp["variant_href"]
            required = comp.get("quantity", 1) or 1
            stock = self.variant_stock(var_href)
            in_stock = stock.get("quantity", 0) or 0
            possible = int(in_stock // required) if required > 0 else 0
            possible_counts.append(possible)
            details.append(
                {
                    "variant_href": var_href,
                    "required": required,
                    "in_stock": in_stock,
                    "possible_by_variant": possible,
                }
            )

        possible_bundle_qty = min(possible_counts) if possible_counts else 0
        return possible_bundle_qty, details

    # ---------------------------------------
    # Retail shift
    # ---------------------------------------
    def create_retailshift(self):
        response = self.client.post(
            "entity/retailshift",
            json={
                "organization": {
                    "meta": {
                        "href": self.org,
                        "type": "organization",
                    }
                },
                "retailStore": {
                    "meta": {
                        "href": self.retailstore,
                        "type": "retailstore",
                    }
                },
            },
        )
        if response.status_code != 200:
            raise Exception("retailshift not created")
        return response.json()["meta"]["href"]

    def close_retailshift(self, href):
        response = self.client.put(
            "entity/retailshift", json={"closeDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        if response.status_code != 200:
            raise Exception("retailshift not closed")
        return True

    # ---------------------------------------
    # Order
    # ---------------------------------------
    def create_order(self, products, store):
        """
        products: positions ro'yxati.
        product() yordamida 'assortment.type' ni 'product' yoki 'bundle' qilib yuborish mumkin.
        """
        payload = {
            "organization": {
                "meta": {
                    "href": self.org,
                    "type": "organization",
                }
            },
            "store": {
                "meta": {
                    "href": store,
                    "type": "store",
                }
            },
            "retailShift": {
                "meta": {
                    "href": active_retailshift(),
                    "type": "retailshift",
                }
            },
            "positions": products,
        }
        response = self.client.post("entity/retaildemand", json=payload)
        if response.status_code != 200:
            raise Exception("order not created")
        return response.json()["meta"]["href"]
