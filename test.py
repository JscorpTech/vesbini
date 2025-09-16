import requests

url = "https://api.moysklad.ru/api/remap/1.2/entity/retaildemand"

payload = {
    "organization": {
        "meta": {
            "href": "https://api.moysklad.ru/api/remap/1.2/entity/organization/0122d460-8198-11f0-0a80-03bb002d25d7",
            "type": "organization",
        }
    },
    "store": {
        "meta": {
            "href": "https://api.moysklad.ru/api/remap/1.2/entity/store/a3bc3936-0d84-11ed-0a80-026d001bdb3f",
            "type": "store",
        }
    },
    "retailShift": {
        "meta": {
            "href": "https://api.moysklad.ru/api/remap/1.2/entity/retailshift/9a700f3a-8bd4-11f0-0a80-141a005f2d5c",
            "type": "retailshift",
        }
    },
    "positions": [
        {
            "quantity": 1,
            "price": 150000,
            "assortment": {
                "meta": {
                    "href": "https://api.moysklad.ru/api/remap/1.2/entity/product/4fe00405-f31c-11ee-0a80-1009002037c0?expand=supplier",
                    "type": "product",
                }
            },
        }
    ],
}
headers = {"authorization": "Bearer 5517f4a54d38fffb0a3ee952c9dd6d2a51f1bd81", "content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
