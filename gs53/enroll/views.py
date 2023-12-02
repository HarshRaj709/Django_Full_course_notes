from django.shortcuts import render,HttpResponseRedirect,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import Registration
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    if request.method=='POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data saved successfully')
    else:
        fm=Registration()
    return render(request,'enroll/signup.html',{'form':fm})


#for login
def user_login(request):
    if not request.user.is_authenticated:  # it will take care that user is already loggined then he will not able to to login page again.
        if request.method=='POST':
            fm = AuthenticationForm(request=request,data=request.POST) #takes 2 arguments request,data
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass) #built in authenticate function takes 2 args username and password

                if user is not None: # if matched then user will get 1
                    login(request,user)
                    messages.success(request, 'Login Successful')
                    # return HttpResponseRedirect('/profile/') #iske liye url sahi hona chaiye but redirect ke liye only name
                    return redirect('profile')                
        else:

            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return redirect('profile')

#user profile
def user_profile(request):
    if request.user.is_authenticated:  #only view profile when you are logined
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return redirect('login')


#logout
def user_logout(request):
    logout(request)  #logout function used to delete current session
    messages.success(request,'Logout successful')
    return redirect('login')