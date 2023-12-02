from django.shortcuts import render,HttpResponse
from django.views import View


# Create your views here.
def home(request):
    return HttpResponse('<h2>THis is function based views.</h2>')

#views through class
#child of View class
class Hom2(View):
    name = 'Ravi'
    def get(self,request):
        # name = 'Ravi'
        # return HttpResponse('<h2>THis is Class based views.</h2>'+name)
        return HttpResponse(self.name)
    

#child of our class 
class Myviewchild(Hom2):
    def get(self,request):
        return HttpResponse(self.name)