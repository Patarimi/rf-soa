from django.db import models
from django.urls import reverse

class Key_Perf(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Components_Type(models.Model):
    name = models.CharField(max_length=200)
    perf_list = models.ManyToManyField(Key_Perf, help_text="select key performances of this component type")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('list_compo', args=[str(self.id)])

class Provider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Techno(models.Model):
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        default=0)
    def __str__(self):
        return self.name

class Component(models.Model):
    doi = models.URLField(max_length=200)
    comp_type = models.ForeignKey(
        Components_Type,
        on_delete=models.CASCADE)
    techno = models.ForeignKey(
        Techno,
        on_delete=models.CASCADE)
    def __str__(self):
        return self.doi
    def get_absolute_url(self):
        return reverse('compo', args=[str(self.id)])
