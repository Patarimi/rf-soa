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
    context_object_name = "item_list"
    template_name = "list.html"

class ListCompo(generic.ListView):
    model = Component
    context_object_name = "item_list"
    template_name = "list.html"
    def get_queryset(self):
        return Component.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ListCompo, self).get_context_data(**kwargs)
        context["title"] = Components_Type.objects.all()[pk]
        return context
