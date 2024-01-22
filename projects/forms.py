from django import forms


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    lead_name = forms.CharField(max_length=100)
