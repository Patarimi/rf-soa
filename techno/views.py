from django.shortcuts import render
from django.views import generic
from techno.models import Components_Type, Component

def index(request):
    context = {
        "compo_num": Component.objects.all().count(),
        "compo_type_num": Components_Type.objects.all().count(),
        }
    return render(request, "index.html", context)

def explore(request):
    
    return render(request, "explore.html")

class ListCompoType(generic.ListView):
    model = Components_Type
    template_name = "list.html"

class ListCompo(generic.ListView):
    model = Component
    template_name = "list.html"
