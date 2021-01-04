from django.test import TestCase
from django.urls import reverse

from .models import Component, Components_Type, Techno, Technos_Type, Provider, Key_Param

class ViewsTest(TestCase):
    def test_static_view(self):
        static_path_list = ('graph', 'index', 'explore')
        app_name = 'techno'
        for path in static_path_list:
            resp = self.client.get(reverse(f'{app_name}:{path}'))
            self.assertEqual(resp.status_code, 200)
    def test_graph(self):
        post_mess = {'comptype':1,
                     'x_axis':3,
                     'y_axis':2,  
                    }
        key_param3 = Key_Param(name_text='third', pk=3)
        key_param3.save()
        key_param2 = Key_Param(name_text='second', pk=2)
        key_param2.save()
        compo_type = Components_Type(name='foo', pk=1)
        compo_type.save()
        resp = self.client.get(reverse('techno:graph'))
        resp = self.client.post(reverse('techno:graph'), post_mess)
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
        tech = Techno(name='28FDSOI', pk=1, techno_type=tech_type, provider=prov)
        tech.save()
        
        compo = Component(doi='https://doi.org/foo',
                          pk=1,
                          comp_type=compo_type,
                          techno=tech,
                          )
        compo.save()
        resp = self.client.get(compo.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
