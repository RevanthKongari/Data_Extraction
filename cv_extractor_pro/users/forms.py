#from collections.abc import Sequence
#from typing import Any
from django import forms
from django.forms.widgets import Widget
from .widgets import CustomClearableFileInput
"""
class MultipleFileInput(forms.ClearableFileInput):
    
    allow_multiple_selected = True
class MultipleFileField(forms.FileField):
    def __init__(self, *args,**kwargs):
        kwargs.setdefault("widget",MultipleFileInput())
        super().__init__(*args,**kwargs)
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data,(list,tuple)):
            result = [single_file_clean(data, initial)for d in data]
        else:
            result=[single_file_clean(data,initial)]
        return result
"""


class CVUploadForm(forms.Form):
    #folder = MultipleFileField()

    #folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),required=True)
    #folder = forms.CharField(max_length=400,widget=forms.HiddenInput())
    #files = forms.CharField(max_length=255,widget=forms.HiddenInput())
    files = forms.FileField(required=True)
    #{{ form.as_p }} 