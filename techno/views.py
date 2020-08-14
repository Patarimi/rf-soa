from django.shortcuts import render
from django.views import generic
from techno.models import Components_Type, Component, Key_Perf
from .forms import GraphFrom
from bokeh.plotting import figure
from bokeh.embed import components

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
        comp_type = Components_Type.objects.get(pk=self.kwargs['type_id'])
        form.instance.comp_type_id = comp_type
        return super().form_valid(form)

def axis_type(axis_name, request):
    try:
        request.POST[axis_name]
        return "log"
    except KeyError:
        return "linear"

def graph(request):
    context = {}
    if request.method == 'POST':
        #form parts
        type_id = request.POST["comptype"]
        y_axis = Key_Perf.objects.filter(components_type = type_id).get(pk=request.POST['y_axis'])
        x_axis = Key_Perf.objects.filter(components_type = type_id).get(pk=request.POST['x_axis'])
        form = GraphFrom(request.POST, type_id=type_id)
        
        #plotting parts
        comp_type = Components_Type.objects.get(pk=type_id)
        plot = figure(
            title = comp_type.name,
            x_axis_label=x_axis.name,
            y_axis_label=y_axis.name,
            x_axis_type=axis_type('x_log_scale', request),
            y_axis_type=axis_type('y_log_scale', request),
            )
        data_set = Component.objects.filter(comp_type_id = type_id).values_list('key_perf')
        x_value, y_value = [], []
        for data, *_ in data_set:
            try:
                x, y = data[x_axis.name], data[y_axis.name]
                x_value.append(float(x))
                y_value.append(float(y))
            except KeyError:
                pass
        plot.circle(x_value, y_value, size=5, color="blue")
        script, div = components(plot)
        context = {
                   'script': script,
                   'div': div
                   }
    else:
        form = GraphFrom(initial={'x_axis':3, 'y_axis':2}, type_id='1')
    context['form'] = form
    return render(request, "graph.html", context)
