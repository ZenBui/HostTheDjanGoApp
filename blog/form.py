from django import forms
from .models import blogForm

class blogRegForm(forms.ModelForm):
    class Meta:
        model = blogForm
        fields = [
            'name',
            'email',
            'numberPhone',
        ]