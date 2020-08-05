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

class CompoCreate(generic.CreateView):
    model = Component
    fields = ['doi',
             'techno',
             'key_perf',
             ]
    template_name = "newcompo.html"
    def form_valid(self, form):
        Comp_Type = Components_Type.objects.get(pk=self.kwargs['type_id'])
        form.instance.comp_type_id = Comp_Type
        return super().form_valid(form)
