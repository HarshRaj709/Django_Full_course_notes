from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from .forms import StudentRegistration

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.success(request,'Data saved successfully')   #shortcut
            messages.add_message(request,messages.SUCCESS,'Your account created Successfully')
            messages.add_message(request,messages.INFO,'Your account info created Successfully')

            #------------------- messages.level----------------------#
            current_level = messages.get_level(request)
            print(current_level)
            messages.set_level(request,messages.DEBUG) # debug ka level km h info se to usko dekhne ke liye humko message ke level ko debug pe set krna hoga.
            current_level = messages.get_level(request)
            print(current_level)
            messages.debug(request,'this is debug')
            #-------------------------------------------------------#
    else: fm=StudentRegistration()
    return render(request,'enroll/home.html',{'form':fm})

# def message(request):
#     messages.success(request,'killu kallan kaliya')
#     # return render(request,'enroll/home.html')
#     # return redirect('home')
#     return HttpResponseRedirect('/')