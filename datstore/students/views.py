from django.shortcuts import render
from .forms import studentforms
from .models import student

# Create your views here.
def form(request):
    if request.method=='POST':
        user = studentforms(request.POST)
        if user.is_valid():
            print('valid')
            name = user.cleaned_data['stuname']
            email = user.cleaned_data['stuemail']
            password = user.cleaned_data['stupassword']
            regi = student(stuname=name,stuemail=email,stupassword=password)
            regi.save()

    else:
        user = studentforms()
    return render(request,'students/form.html',{'use':user})