from django import forms
from .models import Components_Type, Key_Perf

class GraphFrom(forms.Form):
    choices = Components_Type.objects.all().values_list()
    comptype = forms.ChoiceField(choices=choices)
    
    def __init__(self, *args, **kwargs):
        self.type_id = kwargs.pop('type_id')
        super().__init__(*args, **kwargs)
        
        choices = Key_Perf.objects.filter(components_type = self.type_id)
        self.fields['y_axis'] = forms.ChoiceField(choices=choices.values_list())
        self.fields['x_axis'] = forms.ChoiceField(choices=choices.values_list())
