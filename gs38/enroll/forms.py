from django import forms
from django.core import validators

# creating custom validators
#increase reuseability
# def start_with_s(value):
#     if value[0]!='s':
#         raise forms.ValidationError('Name should start with s')

class UserForms(forms.Form):
    # custom validators 
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(error_messages={'required':'Please enter your name','min_length':'chotaa h kya tera'},min_length=4)
    email = forms.EmailField(error_messages={'required':'Please enter your Email','min_length':'10 se bda dalo'},min_length=10)
    password = forms.EmailField(error_messages={'required':'Please enter your Password'})