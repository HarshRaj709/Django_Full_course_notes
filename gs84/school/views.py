from django.shortcuts import render,HttpResponse
from .models import Examcenter,MyExamcenter

# Create your views here.
def home(request):
    exam = Examcenter.objects.all()
    myexam = MyExamcenter.objects.all()
    return render(request,'school/home.html',{'exam':exam,'my':myexam})