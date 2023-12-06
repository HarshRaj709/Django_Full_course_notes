from django.shortcuts import render,HttpResponse
from .forms import Contact
from django.views.generic import FormView,TemplateView

# Create your views here.
class ContactFormView(FormView):
    template_name = 'school/contact.html'       #default nhi h but humko template_name dena hi hpga..
    form_class = Contact        # konse form ko render krna h?
    success_url = '/thankyou/'          #ye bhi dena h ki Form data send hone ke bad kha jaye?
    initial = {'name':'harsh Saahu'}        #placeholder value ki tarah hi h, initially fill ho kr ayega.
    
    def form_valid(self,form):
        # print(form)
        name = form.cleaned_data['name']
        print(name)
        return super().form_valid(form)       #isse humara thankyou link chal rhi h. important because it allows the default behavior defined in the FormView class to be executed.
        # return HttpResponse('thanks')

class ThankyouTemp(TemplateView):
    template_name = 'school/thanks.html'