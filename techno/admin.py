from django.contrib import admin

from .models import Technos_Type, Techno, Provider, Components_Type, Component, Key_Perf, Key_Param

class Key_PerfInline(admin.TabularInline):
    model = Key_Perf
    extra = 1

@admin.register(Component)    
class ComponentAdmin(admin.ModelAdmin):
    inlines = (Key_PerfInline, )
    list_display = ('doi', 'comp_type_id', 'techno')
    list_filter = ['comp_type_id', 'techno']

@admin.register(Key_Param)
class Key_ParamAdmin(admin.ModelAdmin):
    list_display = ('name_text', 'units')

@admin.register(Key_Perf)
class Key_PerfAdmin(admin.ModelAdmin):
    list_display = ('component', 'key_param', 'value')
    list_fiter = ('component', 'key_param')

@admin.register(Techno)
class TechnoAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'node_length', 'techno_type')

admin.site.register(Technos_Type)
admin.site.register(Provider)
admin.site.register(Components_Type)
