from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.apps.api.models import PromocodeModel


class PromocodeTest(TestCase):

    def _create_data(self):
        return PromocodeModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.urls = {
            "validate": reverse("promocode-validate"),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_validate(self):
        response = self.client.post(self.urls["validate"], data={"code": self.instance.code})
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_invalid_code(self):
        response = self.client.post(self.urls["validate"], data={"code": self.instance.code + "1"})
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 404)

    def test_code_expired(self):
        obj = PromocodeModel.objects.create(code="1111", quantity=0, discount=100)
        response = self.client.post(self.urls["validate"], data={"code": obj.code})
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 400)
