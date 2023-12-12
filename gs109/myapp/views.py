from typing import Any
from django.forms.forms import BaseForm
from django.shortcuts import render,HttpResponse
from django.contrib.auth.views import LogoutView,PasswordChangeView
from django.contrib.auth.models import User
from django import forms

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def profile(request):
    return HttpResponse('this is profile page')

# def dashboard(request):
#     return render(request,'myapp/dash.html')

class CustomLogoutView(LogoutView):         #here we inherit LogoutView
    model = User
    template_name = 'myapp/logout.html'
    # success_url='myapp/login.html'        #not working

    def get_context_data(self, **kwargs):
       context= super().get_context_data(**kwargs)
       context['title'] = 'Bahar a gye h'
       context['site'] = 'Harsh ki Site h Chacha'
       context['multiple'] = {'name':self.model.objects.get(pk=2),'class':'btech'}
       return context
    
class CustomizePassword(PasswordChangeView):
    template_name = 'myapp/passchange.html'
    success_url = 'myapp/passsuccess.html'      # otherwise defaut template pe redirect krdega..registration/password_change_done.html, name='password_change_done'
    # success_url = reverse_lazy('password_change_done')     #isme name dala jata h reverse_lazy

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['pass'] = 'ha bhai aa gya swad.'
        return context
    
    def get_form(self, form_class=None):        # here as we not provided any custom form we specified form_class = None.
        form = super().get_form(form_class)
        form.fields['old_password'].widget = forms.TextInput(attrs={'class':'test'})
        # form.labels['old_password'].label = self.label(attrs={'class':'red'})
        return form
