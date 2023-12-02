from django import forms

class Userregister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=False)
    password = forms.CharField()