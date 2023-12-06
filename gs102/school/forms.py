from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['name','password','email']
        widgets = {'name':forms.TextInput(attrs={'class':'mytext'}),
                   'password':forms.PasswordInput(attrs={'class':'mypass'})}