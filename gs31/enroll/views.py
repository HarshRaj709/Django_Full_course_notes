from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import user

# Create your views here.
def thankyou(request):
    return render(request,'enroll/success.html')
def forms(request):
    if request.method == 'POST':
        fm= user(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            print('valid')
            print('name:',name)
            return HttpResponseRedirect('success/success/')
            #return render(request,'enroll/success.html',{'name':name})
        else:
            print('lahsuun')
    else:
        fm=user()
    return render(request,'enroll/froms.html',{'us':fm})