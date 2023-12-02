from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import UserRegistration
from .models import User
from django.contrib import messages

# Create your views here.
def base(request):
    if request.method=='POST':
        user = UserRegistration(request.POST)
        if user.is_valid():
            # name = user.cleaned_data['Name']
            # email = user.cleaned_data['Email']
            # password = user.cleaned_data['Password']
            # regi = User(Name=name,Email=email,Password=password)
            # regi.save()
            user.save()
            

            
    else:
        user = UserRegistration()
    show = User.objects.all() # to show data on table
    return render(request,'enroll/addstudent.html',{'use':user,'shu':show})


def delete(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')   #After the deletion is successful, the view redirects the user to the root URL ('/').
    # return redirect('home') iska bhi use kr sakte the yha pr
    #'/' is the URL where the browser should be redirected. In this case, '/' typically represents the root or home page of your web application.
    
    # return render(request,'enroll/addstudent.html')  esse to wo khali form dedega


def userupdate(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        user = UserRegistration(request.POST, instance=pi)
        if user.is_valid():
            user.save()
            messages.success(request, 'User data updated successfully.') #ye message show kr rha h
            return redirect('home')  #essa krne se humara page update hone ke bad home page pr aajayega
        # HttpResponseRedirect krne se humare current url ke aage add hota h next url-->127.0.0.1:8000/update/25/home
        # But redirect krne se only wahi url leta h jo diya gya ho. --> http://127.0.0.1:8000/
    else:
        pi = User.objects.get(pk=id)
        user = UserRegistration(instance=pi)
    return render(request,'enroll/UpdateUser.html',{'use':user})