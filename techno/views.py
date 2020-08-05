from django.shortcuts import render
from django.views import generic
from techno.models import Components_Type, Component

def index(request):
    context = {
        "compo_num": Component.objects.all().count(),
        "compo_type_num": Components_Type.objects.all().count(),
        }
    return render(request, "index.html", context)

class ListCompoType(generic.ListView):
    model = Components_Type
    context_object_name = "item_list"
    template_name = "list.html"

class ListCompo(generic.ListView):
    model = Component
    context_object_name = "item_list"
    template_name = "list.html"
    def get_queryset(self, **kwargs):
        return Component.objects.filter(comp_type_id = self.kwargs['pk'])
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context["title"] = Components_Type.objects.get(pk=pk)
        return context

class Compo(generic.DetailView):
    model = Component
    template_name = 'component_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Comp = Component.objects.get(pk=self.kwargs['pk'])
        key_perf = eval(Comp.key_perf)
        context["key_perf"] = key_perf
        return context

class CompoCreate(generic.CreateView):
    model = Component
    field = ['doi', 'techno']
    template_name = "newcompo.html"
