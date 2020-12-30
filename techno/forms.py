from django import forms
from django.http import Http404
from django.db.utils import ProgrammingError

from .models import Components_Type, Key_Param

class GraphFrom(forms.Form):
    try:
        choices = Components_Type.objects.all()
        comptype = forms.ChoiceField(choices=choices.values_list())
        x_axis = forms.ChoiceField()
        x_log_scale = forms.BooleanField(required=False)
        y_axis = forms.ChoiceField()
        y_log_scale = forms.BooleanField(required=False)
    except ProgrammingError:
        pass
    
    def __init__(self, *args, **kwargs):
        self.type_id = kwargs.pop('type_id')
        super().__init__(*args, **kwargs)
        
        choices = Key_Param.objects.all().values_list('pk', 'name_text')
        self.fields['y_axis'] = forms.ChoiceField(choices=choices)
        self.fields['x_axis'] = forms.ChoiceField(choices=choices)
