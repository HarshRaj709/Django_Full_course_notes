from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import Student

# Create your views here.
class StudentCreateView(CreateView):
    model = Student                     #isse humara data save ho jata h..
    fields = [field.name for field in Student._meta.fields]
    success_url = '/success/'           # success_url='/'   to return at same page.

    def form_valid(self, form):
        name = form.cleaned_data['name']
        print(name)
        return super().form_valid(form)




class success(TemplateView):
    template_name = 'school/success.html'