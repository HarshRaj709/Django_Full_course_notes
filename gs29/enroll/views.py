from django.shortcuts import render
from .forms import Userregister
# Create your views here.


def forms(request):
    if request.method == 'POST':
        fm = Userregister(request.POST)
        if fm.is_valid():
            print('form is valid')
            name = fm.cleaned_data['name']  # // request.POST['name'] but by this we not get cleaned data
            print('cleaned data:',fm.cleaned_data)
            print('Name:',name)
            password = fm.cleaned_data['password']
            print('password:',password)
            fm=Userregister()
        else:
            print('gadhe')
    else:
        fm=Userregister()
        print('ye humara get request se aya h')
    return render(request,'enroll/forms.html',{'use':fm})