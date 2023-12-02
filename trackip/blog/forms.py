from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post

class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True,label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,label='Last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,label='Email',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:     #to specify our own methods
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'Username'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title','Description']
        widgets = {'Description':forms.Textarea(attrs={'class':'form-control'}),
                   'Title':forms.TextInput(attrs={'class':'form-control'}),
                   }
        