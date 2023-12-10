from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
# def home(request):
#     return HttpResponse('this is home page')

class home(TemplateView):
    template_name = 'registration/home.html'


class Profile(TemplateView):
    model = User
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_user"] = self.model.objects.all() 
        return context
    
class About(TemplateView):
    template_name = 'registration/about.html'

@method_decorator(login_required,name='dispatch')
class Contact(TemplateView):
    template_name = 'registration/contact.html'