from django.shortcuts import render
from .forms import Registration
# Create your views here.

def forms(request):
    if request.method == 'POST':
        user = Registration(request.POST)
        if user.is_valid():
            print('valid data')
            name = user.cleaned_data['Name']
            email = user.cleaned_data['Email']
            passw = user.cleaned_data['Password']
            print(name)
            print(email)
            print(passw)
    else:
        user=Registration()
    return render(request,'enroll/form.html',{'use':user})
