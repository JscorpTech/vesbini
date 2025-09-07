import httpx

from config.env import env


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
        self.store = "2ddf3506-e51d-11ee-0a80-1409003ab718"
        self.org = "0122d460-8198-11f0-0a80-03bb002d25d7"

    def on_request(self, request: httpx.Request):
        request.headers["Accept-Encoding"] = "gzip"
        request.headers["Authorization"] = "Bearer {}".format(self.password)

    def stok(self, codes):
        ids = self.product_ids(codes)
        url = ""
        for _id, _ in ids:
            url += "product=https://api.moysklad.ru/api/remap/1.2/entity/product/{};".format(_id)
        response = self.client.get("report/stock/all?filter={}".format(url))
        rows = response.json().get("rows", [])
        if len(rows) <= 0:
            raise Exception("product not in stock")
        for row in rows:
            code = row["externalCode"]
            quantity = row["quantity"]
            yield code, quantity

    def product_ids(self, codes):
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
            yield row["id"], row["externalCode"]
