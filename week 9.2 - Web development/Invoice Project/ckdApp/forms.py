from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['unit_price','quantity','vat','cogs','gross_income']
