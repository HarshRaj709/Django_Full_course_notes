from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import userregister


# Create your views here.
def thankyou(request):
    return render(request,'enroll/success.html')
def forms(request):
    if request.method =='POST':
        fm = userregister(request.POST)
        if fm.is_valid():
            print('okay')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('name:' ,name)
            print('email:' ,email)
            print('password:' ,password)
            return HttpResponseRedirect('/regi/success/')
            #return render(request,'enroll/success.html',{'nm':name})

        else:
            print('nope')
    else:
        fm = userregister()
    return render(request,'enroll/forms.html',{'form':fm})