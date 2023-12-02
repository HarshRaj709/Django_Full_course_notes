from django.shortcuts import render
from .forms import userform


# Create your views here.
def forms(request):
    if request.method == 'POST':
        user = userform(request.POST)
        if user.is_valid():
            print('form valid')
            print('name:',user.cleaned_data['name'])
            print('pass:',user.cleaned_data['password'])
            print('confirmed:',user.cleaned_data['Re_enter_password'])
        else:
            pass
    else:
        user = userform()
    return render(request,'validators/forms.html',{'use':user})