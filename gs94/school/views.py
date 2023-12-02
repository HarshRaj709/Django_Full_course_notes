from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'school/home.html'      
    #Now using context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] ='Sonam'
        context['roll'] = 101
        # context = {'name':'sonam','roll':101}         #esse extra context nhi chalega wo only upar wale method se dictionary dene pe chlta h.
        return context