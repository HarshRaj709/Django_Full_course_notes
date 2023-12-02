from django import forms

class studentforms(forms.Form):
    name = forms.CharField(initial='harsh1')
    email = forms.EmailField()
    mobile = forms.IntegerField()
    keys = forms.CharField(widget=forms.HiddenInput())