from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'school/Home.html'  #here we have to specified the full path of the custom html file, not only name of html,but default bhi rhega.
    # template_name_suffix = '_get' #then our defalut file name get change with ---> school/student_get.html.
    context_object_name = 'students'    #humne default context ko bhi badal diya h.
    ordering = ['-id']  # here select the order in descending order.
    
    def get_queryset(self):
        return Student.objects.filter(course__icontains='django')       #isse humare only python course wale ayenge without case sensitive.
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user'] == 'harsh':
            template_name = 'school/harsh.html'
        else:
            template_name = self.template_name
        return [template_name]

    