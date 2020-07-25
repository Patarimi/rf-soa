from django.db import models

class Components_Type(models.Model):
    name = models.CharField(max_length=200)
    perf_list = models.CharField(max_length=200)
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.doi
    