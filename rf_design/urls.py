from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'rf'

urlpatterns = [
    path('', views.index, name='index'),
    path('model_ext', views.model_ext, name='model_ext'),
    path('coupler_sizing', views.coupler_sizing, name='coupler_sizing'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)