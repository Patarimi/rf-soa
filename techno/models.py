from django.db import models
from django.urls import reverse

class Key_Param(models.Model):
    UnitsPool = models.TextChoices('UnitsPool', 'Hz W %')
    name_text = models.CharField(max_length=200)
    units = models.CharField(blank=True, choices= UnitsPool.choices, max_length=10)
    def __str__(self):
        return self.name_text
    
class Components_Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'<{self.id}> '+self.name
    def get_absolute_url(self):
        return reverse('list_compo', args=[str(self.id)])

class Provider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Techno(models.Model):
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.name

class Component(models.Model):
    doi = models.URLField(max_length=200)
    comp_type_id = models.ForeignKey(Components_Type, on_delete=models.CASCADE)
    perf_record = models.ManyToManyField(Key_Param, through='Key_Perf')
    techno = models.ForeignKey(Techno, on_delete=models.CASCADE)
    def __str__(self):
        return self.doi.split('/')[-1]
    def get_absolute_url(self):
        return reverse('compo', args=[str(self.id)])

class Key_Perf(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
    key_param = models.ForeignKey(Key_Param, on_delete=models.CASCADE, null=True)
    value = models.FloatField(default=0)
    def __str__(self):
        if (self.key_param.units == '%'):
            form = '2.2f'
        else:
            form = '3.2e'
        return f'{self.key_param}: {self.value : {form}}{self.key_param.units}'
