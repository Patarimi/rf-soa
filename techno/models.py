from django.db import models
from django.urls import reverse

class Key_Param(models.Model):
    UnitsPool = models.TextChoices('UnitsPool', 'Hz W %')
    name_text = models.CharField(max_length=200)
    units = models.CharField(blank=True, choices= UnitsPool.choices, max_length=10)
    def __str__(self):
        return f'{self.name_text} ({self.units})'
    
class Components_Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('techno:list_compo', args=[str(self.id)])

class Provider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Technos_Type(models.Model):
    name_text = models.CharField(max_length=200)
    def __str__(self):
        return self.name_text

class Techno(models.Model):
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=1)
    node_length = models.IntegerField(default=0)
    techno_type = models.ForeignKey(Technos_Type, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name

class Component(models.Model):
    doi = models.URLField(max_length=200)
    comp_type_id = models.ForeignKey(Components_Type, on_delete=models.CASCADE, verbose_name='component type')
    perf_record = models.ManyToManyField(Key_Param, through='Key_Perf')
    techno = models.ForeignKey(Techno, on_delete=models.CASCADE)
    def __str__(self):
        return self.doi.split('/')[-1]
    def get_absolute_url(self):
        return reverse('techno:compo', args=[str(self.id)])

class Key_Perf(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, default=1)
    key_param = models.ForeignKey(Key_Param, on_delete=models.CASCADE, default=1)
    value = models.FloatField(default=0)
    def __str__(self):
        if (self.key_param.units == '%'):
            form = '2.2f'
        else:
            form = '3.2e'
        return f'{self.key_param}: {self.value : {form}}{self.key_param.units}'
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['component', 'key_param'], name='perf_record'),
        ]
