from django import forms

from .models import AdminFacing

class AdminForm(forms.ModelForm):
    class Meta:
        model=AdminFacing
        fields=['app_name','link','points','category','sub_category']
        