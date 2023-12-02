from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registration(UserCreationForm):
    first_name = forms.CharField(required=True,error_messages={'required':'Please Enter Your first name'})
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        error_messages = {'username':{'required':'Please enter your unique username'}}