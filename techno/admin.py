from django.contrib import admin

from .models import Technos_Type, Techno, Provider, Components_Type, Component, Key_Perf, Key_Param

admin.site.register(Technos_Type)
admin.site.register(Techno)
admin.site.register(Provider)
admin.site.register(Components_Type)
admin.site.register(Component)
admin.site.register(Key_Perf)
admin.site.register(Key_Param)
