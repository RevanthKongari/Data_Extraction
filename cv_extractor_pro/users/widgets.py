from django.forms.widgets import ClearableFileInput
class CustomClearableFileInput(ClearableFileInput):
    allow_multiple_selected=True
    def __init__(self, attrs: None):
        super().__init__(attrs)
        if attrs is not None:
            attrs['multiple']= 'multiple'