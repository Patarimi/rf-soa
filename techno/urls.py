from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('explore', views.explore, name="explore"),
    path('list_compo_type', views.ListCompoType.as_view(), name="list_compo_type"),
         ]