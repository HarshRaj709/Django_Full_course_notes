from django import forms
from .models import student

class studentforms(forms.ModelForm):
    class Meta:
        model = student
        fields=['stuid','stuname','stuemail','stupassword']
        labels = {'stuid':'ID','stuname':'Your Name',
                  'stuemail':'Your Email',
                  'stupassword':'Your Password'}
        
        error_messages={'stuname':{'required':'Please enter your name'},
                        'stuemail':{'required':'Please Enter Your Email'}}
        
        widgets = {'stupassword':forms.PasswordInput}