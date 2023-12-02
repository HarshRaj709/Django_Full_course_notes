from django.shortcuts import render
from .forms import userforms

def forms(request):
    if request.method == 'POST':
        user = userforms(request.POST)
        if user.is_valid():
            name = user.cleaned_data['name']
            print('Agree:',user.cleaned_data['agree'])
            print('valid')
            print('name:',name)
            #return render(request,'enroll/success.html',{'name':name})
        else:
            print('lahsumun')
    else:
        user= userforms()
    return render(request,'enroll/forms.html',{'forms':user})
