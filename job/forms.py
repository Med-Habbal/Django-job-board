from django import forms

from .models import Apply, Job

class ApplyForms(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_lettre']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','slug')