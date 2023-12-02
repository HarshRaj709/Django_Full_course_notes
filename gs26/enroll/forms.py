from django import forms

class userforms(forms.Form):
    email = forms.EmailField()
    First_name = forms.CharField(initial = 'harsh',help_text = 'hello g') #_underscore space me convert ho jayega
    names = forms.CharField(initial='harsh mahahraj') 