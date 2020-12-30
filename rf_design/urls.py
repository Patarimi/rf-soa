from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'rf'

urlpatterns = [
    path('', views.index, name='index'),
    path('calc', views.index, name='calc'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)