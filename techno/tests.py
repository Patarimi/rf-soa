from django.test import TestCase
from django.urls import reverse

from .views import graph

class GraphTest(TestCase):
    def test_path(self):
        response = self.client.get(reverse('techno:graph'))
        self.assertEqual(response.status_code, 200)
