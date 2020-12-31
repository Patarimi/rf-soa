from django.test import TestCase
from django.urls import reverse

from .views import index

class TestViews(TestCase):
    def test_index(self):
        resp = self.client.get(reverse('rf:index'))
        self.assertEqual(resp.status_code, 200) 
