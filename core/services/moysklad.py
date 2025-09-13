from datetime import date, datetime

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

    def product(self, quantity, amount, href):
        return {
            "quantity": quantity,
            "price": amount,
            "assortment": {
                "meta": {
                    "href": href,
                    "type": "product",
                }
            },
        }

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

    def stok(self, codes=[], hrefs=[]):
        if len(codes) == 0 and len(hrefs) == 0:
            raise Exception("codes yoki hrefs kiritish majburiy")
        if len(hrefs) <= 0:
            hrefs = self.products_href(codes)
        url = ""
        for href, _ in hrefs:
            url += "product={};".format(href)
        response = self.client.get("report/stock/all?filter={}".format(url))
        rows = response.json().get("rows", [])
        if len(rows) <= 0:
            raise Exception("product not in stock")
        for row in rows:
            code = row["externalCode"]
            quantity = row["quantity"]
            yield code, quantity, row["meta"]["href"]

    def products_href(self, codes):
        # k4ybiRBqgRTB35zl76-Ol0
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

    def create_retailshift(self):
        response = self.client.post(
            "/entity/retailshift",
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
            "/entity/retailshift", json={"closeDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        if response.status_code != 200:
            raise Exception("retailshift not closed")
        return True

    def create_order(self, products, store):
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
        print(payload)
        response = self.client.post("/entity/retaildemand", json=payload)
        print(response.json())
        if response.status_code != 200:
            raise Exception("order not created")
        return response.json()["meta"]["href"]
