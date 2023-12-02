from django.shortcuts import render
from .forms import Userforms
from .models import Employee
# Create your views here.

def forms(request):
    if request.method == 'POST':
        user = Userforms(request.POST)
        if user.is_valid():
            print('valid data')
            name = user.cleaned_data['name']
            email = user.cleaned_data['Email']
            passw = user.cleaned_data['Password']

            reg = Employee(Name=name,Email=email,Password=passw)  #by this we can update our data
            reg.save()
            # reg = Employee(id=2)
            # reg.delete()           #by this we can delete data
            

    else:
        user=Userforms()
    return render(request,'enroll/form.html',{'use':user})
