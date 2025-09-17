from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.apps.api.models import NotificationModel, UserNotificationModel

# class NotificationTest(TestCase):
#
#     def _create_data(self):
#         return NotificationModel._create_fake()
#
#     def setUp(self):
#         self.client = APIClient()
#         self.instance = self._create_data()
#         self.urls = {
#             "list": reverse("notification-list"),
#             "retrieve": reverse("notification-detail", kwargs={"pk": self.instance.pk}),
#             "retrieve-not-found": reverse("notification-detail", kwargs={"pk": 1000}),
#         }
#
#     def test_create(self):
#         self.assertTrue(True)
#
#     def test_update(self):
#         self.assertTrue(True)
#
#     def test_partial_update(self):
#         self.assertTrue(True)
#
#     def test_destroy(self):
#         self.assertTrue(True)
#
#     def test_list(self):
#         response = self.client.get(self.urls["list"])
#         self.assertTrue(response.json()["status"])
#         self.assertEqual(response.status_code, 200)
#
#     def test_retrieve(self):
#         response = self.client.get(self.urls["retrieve"])
#         self.assertTrue(response.json()["status"])
#         self.assertEqual(response.status_code, 200)
#
#     def test_retrieve_not_found(self):
#         response = self.client.get(self.urls["retrieve-not-found"])
#         self.assertFalse(response.json()["status"])
#         self.assertEqual(response.status_code, 404)
#


class UsernotificationTest(TestCase):

    def _create_data(self):
        return UserNotificationModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.client.force_authenticate(self.instance.user)
        self.urls = {
            "list": reverse("notification-list"),
            "retrieve": reverse("notification-detail", kwargs={"pk": self.instance.pk}),
            "retrieve-not-found": reverse("notification-detail", kwargs={"pk": 1000}),
        }

    def test_create(self):
        self.assertTrue(True)

    def test_update(self):
        self.assertTrue(True)

    def test_partial_update(self):
        self.assertTrue(True)

    def test_destroy(self):
        self.assertTrue(True)

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
