from django.test import TestCase
from django.urls import reverse

from .views import graph
from .models import Component, Components_Type, Techno, Technos_Type, Provider

class ViewsTest(TestCase):
    def test_techno_path(self):
        techno_path_list = ('graph', 'index', 'explore')
        for path in techno_path_list:
            resp = self.client.get(reverse(f'techno:{path}'))
            self.assertEqual(resp.status_code, 200)       

class ModelTest(TestCase):
    def test_components_type(self):
        compo_type = Components_Type(name='foo', pk=1)
        compo_type.save()
        resp = self.client.get(compo_type.get_absolute_url())
        self.assertEqual(resp.status_code, 200) 
    def test_component(self):
        compo_type = Components_Type(name='foo', pk=1)
        compo_type.save()
        tech_type = Technos_Type(name_text='CMOS', pk=1)
        tech_type.save()
        prov = Provider(name='elec')
        prov.save()
        tech = Techno(name='28FDSOI', id=1, techno_type=tech_type, provider=prov)
        tech.save()
        
        compo = Component(doi='https://doi.org/foo',
                          pk=1,
                          comp_type_id=compo_type,
                          techno=tech,
                          )
        compo.save()
        resp = self.client.get(compo.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
