from django import forms
from .models import Components_Type, Key_Param

class GraphFrom(forms.Form):
    choices = Components_Type.objects.all().values_list()
    comptype = forms.ChoiceField(choices=choices)
    x_axis = forms.ChoiceField()
    x_log_scale = forms.BooleanField(required=False)
    y_axis = forms.ChoiceField()
    y_log_scale = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        self.type_id = kwargs.pop('type_id')
        super().__init__(*args, **kwargs)
        
        choices = Key_Param.objects.all().values_list('pk', 'name_text')
        self.fields['y_axis'] = forms.ChoiceField(choices=choices)
        self.fields['x_axis'] = forms.ChoiceField(choices=choices)
