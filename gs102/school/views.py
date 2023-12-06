from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import Student
from django import forms
from .forms import StudentForm

#Create your views here.
# class StudentCreateView(CreateView):
#     model = Student                     #isse humara data save ho jata h..
#     fields = [field.name for field in Student._meta.fields]
#     success_url = '/success/'           # success_url='/'   to return at same page.
#     # agar hum template ka name defined krenge to Default name lega -----'school/student_form.html'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
#         return form

class StudentCreateView(CreateView):
    form_class = StudentForm
    success_url = '/success/'

class success(TemplateView):
    template_name = 'school/success.html'