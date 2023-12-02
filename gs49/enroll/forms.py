from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Student_name','Email','Password']

class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['Teacher_name','Email','Password']