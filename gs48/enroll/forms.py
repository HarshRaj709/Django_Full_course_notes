from django import forms
from .models import UserModel

class UserForms(forms.ModelForm):
    class Meta:
        model = UserModel
        # fields = ['Name','Email','Password']
        fields = '__all__' #esse sare aajyenge models.py ke
        # exclude = ['Name']  #esse name nhi ayega
        widgets = {'Password':forms.PasswordInput}
