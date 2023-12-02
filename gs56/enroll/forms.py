from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','date_joined','last_login']


class AdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields = '__all__' #['username','first_name','last_name','email','date_joined','last_login','is_active','is_staff',]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']