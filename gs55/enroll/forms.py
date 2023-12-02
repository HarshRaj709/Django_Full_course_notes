from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    # roll_no = forms.IntegerField(label='Roll no',required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True,label='*last name')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email'] #,'roll_no'

class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields = ['username','first_name','last_name','last_name','email','date_joined','last_login','is_active','is_staff']