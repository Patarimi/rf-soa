from django.test import TestCase
from django.urls import reverse

from . import views

class ViewsTest(TestCase):
    def test_static_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)