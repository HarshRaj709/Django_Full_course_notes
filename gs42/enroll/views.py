from django.shortcuts import render
from .forms import UserRegistration
from .models import registration

# Create your views here.
def forms(request):
    if request.method == 'POST':
        user = UserRegistration(request.POST)
        if user.is_valid():
            print('valid')
            name = user.cleaned_data['Name']
            email = user.cleaned_data['Email']
            passw = user.cleaned_data['Password']

            regi = registration(Name=name,Email=email,Password=passw)
            regi.save()  #regi.save(commit=True/False) True hoe pe save krga only

            #--------------------- DATA UPDATION THROUGH INSTANCE ------------------------------#

            # killu = registration.objects.get(pk=1) PK == PRIMARY KEY  YHI PE HUMNE MODELS KA REGISTRATION LE LIYA...
            # user = UserRegistration(request.POST, instance=killu)
            # if user.is_valid():
            #     user.save()
    else:
        user = UserRegistration()
    return render(request,'enroll/home.html',{'use':user})