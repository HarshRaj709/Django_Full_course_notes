from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.

class Redirects(RedirectView):
    url = '/'

# class redirect(RedirectView):
#     url = '/'

class redirect(RedirectView):
    pattern_name = 'template_data'
    query_string = True #bydefault False            ise humara link ke aage ke character delete nhi honge.