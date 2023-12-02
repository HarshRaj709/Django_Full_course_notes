from django import forms
from .models import Employee
from django.core import validators


class Registration(forms.ModelForm):
    Name = forms.CharField(max_length=50,required = False)  #high preference than models.py declaration
    class Meta:
        model = Employee
        fields = ['Name','Email','Password']

        
        labels = {'Name':'Your Name'}

        help_texts ={'Name':'Enter Your FUll name:'}

        error_messages = {'Name':{'required':'naame likho chacha','max_length':'chota kro'},
                          'Email':{'required':'bharna jaruri h'}}
        
        widgets = {'Password':forms.PasswordInput,
                   'Name':forms.TextInput(attrs={'class':'myclass','placeholder':'harsh sahu'})}

