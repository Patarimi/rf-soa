from django.test import TestCase
from django.urls import reverse

from .views import index

class TestViews(TestCase):
    def test_static_view(self):
        static_path_list = ('coupler_sizing', 'index', 'model_ext')
        app_name = 'rf'
        for path in static_path_list:
            resp = self.client.get(reverse(f'{app_name}:{path}'))
            self.assertEqual(resp.status_code, 200)  
        
