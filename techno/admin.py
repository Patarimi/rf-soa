from django.contrib import admin

from .models import Techno, Provider, Components_Type, Component

admin.site.register(Techno)
admin.site.register(Provider)
admin.site.register(Components_Type)
admin.site.register(Component)
