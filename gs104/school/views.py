from typing import Any
from django.shortcuts import render
from .models import Student
from django.views.generic import CreateView,TemplateView,UpdateView,ListView
from django import forms

# Create your views here.
class StudentCreate(CreateView):
    model = Student
    template_name = 'school/user.html'
    success_url = '/success/'
    fields = [field.name for field in Student._meta.fields]
    # context_object_name = 'stu'       #not working...

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'mytext'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class StudentUpdate(UpdateView):
    model = Student
    fields = [field.name for field in Student._meta.fields]
    # default template name = school/student_form.html
    template_name = 'school/update.html'
    success_url = '/updated/'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'mytext'})
        form.fields['password'].widget = forms.PasswordInput(render_value=True,attrs={'class':'mypass'})
        return form

class updated(TemplateView):
    pass


class Success(TemplateView):
    model = Student
    template_name = 'school/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = self.model.objects.all()
        return context


class Allstudents(ListView):
    model = Student
    template_name = 'school/allstudent.html'
    context_object_name = 'students'