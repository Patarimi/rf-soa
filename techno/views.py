from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from techno.models import Components_Type, Component, Key_Param, Key_Perf
from .forms import GraphFrom, ComponentForm, PerfInline
from bokeh.plotting import figure
from bokeh.embed import components

def index(request):
    context = {
        "compo_num": Component.objects.all().count(),
        "compo_type_num": Components_Type.objects.all().count(),
        }
    return render(request, "techno/index.html", context)

class ListCompoType(generic.ListView):
    model = Components_Type
    context_object_name = "item_list"
    template_name = "techno/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Component Type'
        return context

class ListCompo(generic.ListView):
    model = Component
    context_object_name = "item_list"
    template_name = "techno/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Components_Type.objects.get(id = self.kwargs['pk'])
        return context
    def get_queryset(self, **kwargs):
        return Component.objects.filter(comp_type_id= self.kwargs['pk'])

class Compo(generic.DetailView):
    model = Component
    template_name = 'techno/component_detail.html'
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['key_perf'] = Key_Perf.objects.filter(component_id=self.kwargs['pk'])
       return context

class CompoCreate(LoginRequiredMixin, generic.View):
    form_class = ComponentForm
    inline_formset = PerfInline
    template_name = "techno/newcompo.html"
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        formset = self.inline_formset(instance=Component())
        return render(request, self.template_name, {'form':form, 'formset':formset})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        formset = self.inline_formset(request.POST, instance=Component())
        if form.is_valid() and formset.is_valid():
            entity = form.save(commit=True)
            formset.instance = entity
            formset.save()
        return render(request, self.template_name, {'form':form, 'formset':formset})

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
        x_id = request.POST['x_axis']
        y_id = request.POST['y_axis']
        key_param_q = Key_Param.objects
        x_axis = key_param_q.get(pk=x_id)
        y_axis = key_param_q.get(pk=y_id)
        form = GraphFrom(request.POST, type_id=type_id)
        
        #plotting parts
        comp_type = Components_Type.objects.get(pk=type_id)
        plot = figure(
            title = comp_type.name,
            x_axis_label=f"{x_axis.name_text} ({x_axis.units})",
            y_axis_label=f"{y_axis.name_text} ({y_axis.units})",
            x_axis_type=axis_type('x_log_scale', request),
            y_axis_type=axis_type('y_log_scale', request),
            )
        data_id = Component.objects.filter(comp_type_id=type_id, perf_record=x_id).values_list('pk')
        data_set = Key_Perf.objects.filter(key_param__in=[x_id, y_id])
        x_value, y_value = [], []
        for data in data_id:
            try:
                x = data_set.get(component_id=data, key_param_id=x_id).value
                y = data_set.get(component_id=data, key_param_id=y_id).value
                x_value.append(float(x))
                y_value.append(float(y))
            except (KeyError, Key_Perf.DoesNotExist):
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
    return render(request, "techno/graph.html", context)
