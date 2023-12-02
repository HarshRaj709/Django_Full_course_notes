from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from .forms import UserForm
from django.contrib import messages
from .models import User
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.
class Home(TemplateView):
    template_name='enroll/home.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = UserForm()
        info = User.objects.all()
        context = {'form':fm,'info':info}
        return context
    
    def post(self,request):
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

        
class UserInfoEdit(View):
    def get(self,request,pk):
        info = User.objects.get(pk=pk)
        fm = UserForm(instance=info)
        return render(request,'enroll/infoupdate.html',{'form':fm,'info':info})
    
    def post(self,request,pk):
        info = User.objects.get(pk=pk)
        fm = UserForm(request.POST,instance=info)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Updated Successfully')
        return redirect('home')
    
# class userdelete(View):
#     def post(self,request,id):
#         user = User.objects.get(id=id)
#         user.delete()
#         messages.success(request,'User deleted Successfully')
#         return redirect('home')

class userdelete(RedirectView):
    url = '/'
    def get_redirect_url(self,*args,**kwargs):
        #   print(kwargs)
        pi = kwargs['id']     #to get id
        User.objects.get(pk=pi).delete()
        return super().get_redirect_url(*args,**kwargs)