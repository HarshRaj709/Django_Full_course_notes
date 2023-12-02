from .models import User
from django import forms


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name','Email','Password']
        error_messages = {'Name':{'required':'Please Enter Your Name'},
                          'Email':{'required':'Please Enter Your Email'},
                          'Password':{'required':'Please Enter Your Password'}
                          }
        widgets = {'Password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
                   'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Harsh Sahu'}),
                   'Email':forms.TextInput(attrs={'class':'form-control'})}