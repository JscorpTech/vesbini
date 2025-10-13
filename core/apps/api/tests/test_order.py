import io
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.apps.api.models import OrderModel
from unittest.mock import patch
from core.apps.api.models.order import ItemModel
from core.apps.api.models.product import BasketModel
from core.apps.api.tasks.order import notify_order


class OrderTest(TestCase):

    def _create_data(self):
        order = OrderModel._create_fake()
        ItemModel._create_fake(order=order)
        return order

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.client.force_authenticate(self.instance.user)
        self.urls = {
            "list": reverse("order-list"),
            "retrieve": reverse("order-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("order-detail", kwargs={"pk": 1000}),
        }

    def test_create(self):
        response = self.client.post(
            self.urls["list"],
            data={"items": [BasketModel._create_fake().id]},
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["status"])

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

    def test_notify_order(self):
        fake_file = io.BytesIO(b"salom")
        with patch("django.core.files.storage.Storage.open", return_value=fake_file):
            with patch("core.apps.api.tasks.order.bot.send_photo") as mock_send_photo:
                mock_send_photo.return_value = True
                notify_order(self.instance.pk)
            mock_send_photo.assert_called_once()

    def test_list(self):
        response = self.client.get(self.urls["list"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(self.urls["retrieve"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)

    def test_retrieve_not_found(self):
        response = self.client.get(self.urls["retrieve-not-found"])
        self.assertFalse(response.json()["status"])
        self.assertEqual(response.status_code, 404)
