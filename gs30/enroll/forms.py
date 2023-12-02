from django import forms

class userregister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())  #This widget will render the password input as a password field on the HTML form, which means the input characters will be masked for security.