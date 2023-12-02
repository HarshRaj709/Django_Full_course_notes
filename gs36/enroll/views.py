from django.shortcuts import render
from .forms import UserForms

def forms(request):
    if request.method == 'POST':
        user = UserForms(request.POST)
        if user.is_valid():
            name = user.cleaned_data['name']
            print('valid')
            print('name:',name)
            print('email:',user.cleaned_data['email'])
            # return render(request,'enroll/success.html',{'name':name})
        else:
            print('lahsumun')
    else:
        user= UserForms()
    return render(request,'enroll/forms.html',{'forms':user})
