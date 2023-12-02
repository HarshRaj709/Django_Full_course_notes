from django import forms

class UserForms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=50, min_length=5, widget=forms.PasswordInput)

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than 4 characters')
        return valname

    def clean_password(self):
        password = self.cleaned_data['password']
        required_chars = ('@', '!')

        # if any(char in password for char in required_chars):
        for char in required_chars:
            if char in password:
                break  # At least one special character found
            else:
                raise forms.ValidationError('Password must include "@" and "!" in it')

        #Check for at least one number
        if not any(hulu.isdigit() for hulu in password):
            raise forms.ValidationError('Password must include at least one number.')
        
        return password
