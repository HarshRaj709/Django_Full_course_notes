from django import forms

class Userforms(forms.Form):
    name = forms.CharField(label='Name',error_messages={'required':'Please fill your Name here'})
    Email = forms.EmailField(error_messages={'required':'Please fill your Email here'})
    Password = forms.CharField(widget=forms.PasswordInput)
