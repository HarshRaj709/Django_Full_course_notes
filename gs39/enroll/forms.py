from django import forms
from django.core import validators

class UserForms(forms.Form):
    error_css_class = 'error'   #essa krne se <tr me class> aaajata jisse hum easily target krsakte h.
    required_css_class = 'required'  #esse krne se <tr class="required error"> required error aane pe hi target krsakte h.
    name = forms.CharField(error_messages={'required':'Please enter your name','min_length':'chotaa h kya tera'},min_length=4)
    email = forms.EmailField(error_messages={'required':'Please enter your Email','min_length':'10 se bda dalo'},min_length=10)
    password = forms.EmailField(error_messages={'required':'Please enter your Password'})