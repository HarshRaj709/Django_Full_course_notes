from django import forms
from django.core import validators
    
class userform(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(3)],label='Name')
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'email'}))
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
    Re_enter_password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        passw = self.cleaned_data['password']
        reenter = self.cleaned_data['Re_enter_password']

        if passw != reenter:
            raise forms.ValidationError('password not matched')