from django import forms

class user(forms.Form):
    name=forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    