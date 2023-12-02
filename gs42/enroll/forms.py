from django import forms
from .models import registration


class UserRegistration(forms.ModelForm):
    class Meta:
        model = registration
        fields=['Name','Email','Password']

        widgets = {'Name':forms.TextInput(attrs={'class':'Name','placeholder':'Harsh Sahu'}),'Password':forms.PasswordInput}

