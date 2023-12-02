from .models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name','Email','Password']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Harsh sahu'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
