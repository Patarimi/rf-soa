from django.contrib import admin

from .models import Technos_Type, Techno, Provider, Components_Type, Component, Key_Perf, Key_Param

class Key_PerfInline(admin.TabularInline):
    model = Key_Perf
    extra = 3
    
class ComponentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description', {'fields':['doi', 'comp_type_id', 'techno']}),
        #('Performances', {'fields':['perf_record'], 'classes':['collapse']}),
    ]
    list_display = ('doi', 'comp_type_id', 'techno')
    list_filter = ['comp_type_id', 'techno']

class Key_ParamAdmin(admin.ModelAdmin):
    list_display = ('name_text', 'units')

class Key_PerfAdmin(admin.ModelAdmin):
    list_display = ('component', 'key_param', 'value')
    list_fiter = ('component', 'key_param')

class TechnoAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'node_length', 'techno_type')

admin.site.register(Technos_Type)
admin.site.register(Techno, TechnoAdmin)
admin.site.register(Provider)
admin.site.register(Components_Type)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Key_Perf, Key_PerfAdmin)
admin.site.register(Key_Param, Key_ParamAdmin)
