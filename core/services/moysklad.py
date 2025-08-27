import base64
import json
from pprint import pprint

import requests


class MoySklad:
    def __init__(self) -> None:
        # INFO: base_uri https://api.moysklad.ru/api/remap/1.2
        self.client = requests.Session()
        self.client.headers = {"Accept-Encoding": "gzip"}
        self.base_uri = "https://api.moysklad.ru/api/remap/1.2"
        self.login = "sotuv@vesbini"
        self.password = "5517f4a54d38fffb0a3ee952c9dd6d2a51f1bd81"
        self.products()

    def _path(self, path: str) -> str:
        return f"{self.base_uri}/{path}"

    def _basic_token(self):
        return base64.b64encode(f"{self.login}:{self.password}".encode("utf-8"))

    def _token(self):
        token = self._basic_token()
        response = self.client.post(self._path("security/token"), headers={"Authorization": f"Basic {token}"})
        print(response.json())

    def variant(self):
        response = self.client.get(
            "https://api.moysklad.ru/api/remap/1.2/report/stock/all?filter=product="
            + self._path("entity/product/3d33ddaf-5e56-11f0-0a80-01f4001b81ae"),
            headers={"Authorization": "Bearer 5517f4a54d38fffb0a3ee952c9dd6d2a51f1bd81"},
        )
        with open("res.json", "w") as file:
            json.dump(response.json(), file, indent=4)

    def products(self):
        response = self.client.get(
            "https://api.moysklad.ru/api/remap/1.2/report/stock/all?filter=product="
            + self._path("entity/product/3d33ddaf-5e56-11f0-0a80-01f4001b81ae"),
            headers={"Authorization": "Bearer 5517f4a54d38fffb0a3ee952c9dd6d2a51f1bd81"},
        )
        print(response.request.url)
        with open("res.json", "w") as file:
            json.dump(response.json(), file, indent=4)
