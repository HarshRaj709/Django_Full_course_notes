from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)   #by specifying here we can make that field required
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']  #ye username,first_name ye sab User se aarha h.
        