from typing import Any
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView,DetailView


class Studentlist(ListView):
    model = Student
    template_name = 'school/home.html'
    context_object_name = 'students'

class StudentDetails(DetailView):
    model = Student
    template_name = 'school/harsh.html'      #default---student_detail.html
    # context_object_name = 'stu'        #default---student       {{stu.id}}
    pk_url_kwarg = 'id'         #agar humko urls me pk ki jagah 'id' likhna h to hume yha pe changes krna hoga..

    #ab iske methods

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)

        context['all_students'] = self.model.objects.all().order_by('name')
        return context

    
    

    