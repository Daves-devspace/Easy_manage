from django import forms
from .models import ClassTermFee


class TermFeeForm(forms.ModelForm):
    class Meta:
        model = ClassTermFee
        fields = ['grade', 'term_fee']  # Fields to include in the form
        