from django import forms

class UserForms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=50, min_length=5, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        name = self.cleaned_data['name']
        voteemail = self.cleaned_data['email']
        # password = self.cleaned_data['password']
        if len(name)<4:
            raise forms.ValidationError('enter more than 4 characters')
        if len(voteemail)<10:
            raise forms.ValidationError('enter more than 10 characters')
