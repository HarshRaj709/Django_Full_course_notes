from django.shortcuts import render
from .forms import UserForms

# Create your views here.
def home(request):
    if request.method=='POST':
        user = UserForms(request.POST)
        if user.is_valid():
            name = user.cleaned_data['name']
            email = user.cleaned_data['email']
            passw = user.cleaned_data['password']

            print('name:',name)
            print('email:',email)
            print('password:',passw)
            return render(request,'html/success.html',{'nm':name})
    else:
        user = UserForms()
    return render(request,'html/home.html',{'use':user})