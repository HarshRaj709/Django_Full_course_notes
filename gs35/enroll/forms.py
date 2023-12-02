from django import forms

class UserForms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=50, min_length=5, widget=forms.PasswordInput)

    #full form validation in single function

    def clean(self):
        cleaned_data=super().clean()
        name = self.cleaned_data['name']
        voteemail = self.cleaned_data['email']
        # password = self.cleaned_data['password']
        if len(name)<4:
            raise forms.ValidationError('enter more than 40 characters')
        if len(voteemail)<10:
            raise forms.ValidationError('enter more than 10 characters')
        
    # single validation at a time

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name)<4:
    #         raise forms.ValidationError('bibo the baby')
    #     return name
