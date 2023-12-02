from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method=='POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'user created successfully, Now you can do login')
    else:
        fm=SignupForm()
    return render(request,'enroll/signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logined successfully')
                    return redirect('profile')
        else:
            fm=AuthenticationForm()            
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return redirect('login')

def user_logout(request):          #same function name se aap custom function nahi bna sakte ho prabhu
    logout(request)
    return redirect('login')

def password1(request):
    if request.method=='POST':
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'Password changed successfully')
            return redirect('login')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request,'enroll/change.html',{'form':fm})

def password2(request):
    if request.method == 'POST':
        fm = SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'Password changed successfully')
            return redirect('login')
    else:
        fm = SetPasswordForm(user=request.user)
    return render(request,'enroll/change1.html',{'form':fm})
