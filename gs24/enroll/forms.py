from django import forms

class userforms(forms.Form):
    names = forms.CharField()
    email = forms.EmailField()
    First_name = forms.CharField()  #_underscore space me convert ho jayega