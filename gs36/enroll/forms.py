from django import forms
from django.core import validators

# creating custom validators
#increase reuseability
def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError('Name should start with s')

class UserForms(forms.Form):
    # custom validators 
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(validators=[start_with_s])
    email = forms.EmailField()