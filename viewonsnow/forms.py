from django import forms

from .models import Snow

class SnowCreateForm(forms.ModelForm):
    """
    Index for snow app, Main window
    """
    class Meta:
        model = Snow
        fields = ['input_before_snow',
                 ]