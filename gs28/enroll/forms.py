from django import forms

class studentforms(forms.Form):
    name = forms.CharField(label='Your Name',initial='harsh1',label_suffix='#',required=False,disabled=True
                           ,help_text = 'limit 70 char')