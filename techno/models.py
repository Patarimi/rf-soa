from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.urls import reverse

class KeyPerfField(models.Field):
    description = "list of key performances of a component"
    
    def __init__(self, *args, **kwargs):
        try:
            if kwargs['comp_type_id'] > 0:
                _comp_type = Components_Type.objects.select_related('perf_list').get(id=kwargs['comp_type_id'])
                self.key_perf_list = _comp_type.perf_list
            del kwargs['comp_type_id']
        except KeyError:
            pass
        super(KeyPerfField, self).__init__(*args, **kwargs)

    def __create_dict(self, value_str):
        table = re.split("[{},]", value_str)
        dic = dict()
        for pair_str in table:
            if pair_str != '':
                pair = re.split(':', pair_str.strip(" '\""))
                fl = float(pair[1])
                dic[pair[0].strip(" '\"")] = fl
        return dic

    def deconstruct(self):
        name, path, args, kwargs = super(KeyPerfField, self).deconstruct()
        try:
            del kwargs['comp_type_id']
        except KeyError:
            pass
        return name, path, args, kwargs
    
    def db_type(self, connection):
        return "keyperf"
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.__create_dict(value)

    def to_python(self, value):
        if isinstance(value, dict):
            return value
        if value is None:
            return value
        return self.__create_dict(value)

    def get_prep_value(self, value_dic):
        out_str = "{"
        for key in value_dic:
            out_str += f"'{key}': {value_dic[key]},"
        return out_str.strip(',')+"}"

    def db_internal_type(self):
        return 'CharField'

class Key_Perf(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Components_Type(models.Model):
    name = models.CharField(max_length=200)
    perf_list = models.ManyToManyField(Key_Perf, help_text="select key performances of this component type")
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

class ComponentManager(models.Manager):
    def create_component(self, compo_type_id):
        return self.create(compo_type_id)

class Component(models.Model):
    doi = models.URLField(max_length=200)
    comp_type_id = models.ForeignKey(Components_Type, on_delete=models.CASCADE)
    key_perf = HStoreField()
    techno = models.ForeignKey(Techno, on_delete=models.CASCADE)
    def __str__(self):
        return self.doi
    def get_absolute_url(self):
        return reverse('compo', args=[str(self.id)])
