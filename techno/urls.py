from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('explore', views.ListCompoType.as_view(), name="explore"),
    path('list_compo/<int:pk>', views.ListCompo.as_view(), name="list_compo"),
    path('compo/<int:pk>', views.Compo.as_view(), name="compo"),
    path('compo_create/<int:type_id>', views.CompoCreate.as_view(), name="newcompo")
         ]
