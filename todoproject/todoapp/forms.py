from . models import taski
from django import forms
class todoform(forms.ModelForm):
    class Meta:
        model=taski
        fields=['name','priority','date']