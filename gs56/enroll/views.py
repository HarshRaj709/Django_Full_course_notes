from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import UserProfileForm,SignUpForm,AdminProfileForm
from django.contrib.auth.models import User     #used to show other Users in admin pannel

# Create your views here.
def UserSignup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST) #only takes data from  the forms
        if fm.is_valid():
            fm.save()
            messages.success(request,'User Created successfully')
            messages.success(request,'Please go to Login Page to further proceed.')
    else:
        fm=SignUpForm()
    return render(request,'enroll/Usersignup.html',{'form':fm})


def Userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                ram = authenticate(username = uname,password = upass)
                if ram is not None:
                    login(request,ram)
                    messages.success(request,'User logined successfully')
                    return redirect('profile')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return redirect('profile')

def Userlogout(request):
    logout(request)         #logout takes 1 argument
    return redirect('login')


def UserProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # if request.user.is_superuser:
            #     fm = AdminProfileForm(request.POST,instance=request.user)
            #     if fm.is_valid():
            #         fm.save()
            #         messages.success(request,'Admin Data saved Successfully')
            # else:
            #     fm = UserProfileForm(request.POST,instance=request.user)
            #     if fm.is_valid:
            #         fm.save()
            #         messages.success(request,'User Data saved Successfully')
            if request.user.is_superuser:
                fm = AdminProfileForm(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm = UserProfileForm(request.POST,instance=request.user)
            if fm.is_valid:
                fm.save()
                messages.success(request,'User Data saved Successfully')
        else:
            if request.user.is_superuser == True:
                fm = AdminProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                fm = UserProfileForm(instance=request.user) #esse hi usme data show krega nhi to blank ayega
                users = None
        return render(request,'enroll/profile.html',{'form':fm,'users':users})
    else:
        return redirect('login')


def password1(request):
    if request.method == 'POST':
        fm = SetPasswordForm(user=request.user,data = request.POST)
        if fm.is_valid():
            update_session_auth_hash(request,fm.user)
            fm.save()
            messages.success(request,'Password change successfully')
            return redirect('login')
    else:
        fm = SetPasswordForm(user=request.user) 
    return render(request,'enroll/password.html',{'form':fm})



def userdetails(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        if request.method == 'POST':
            fm = AdminProfileForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Data edited successfully by admin')
        else:
            fm = AdminProfileForm(instance=pi)
        return render(request,'enroll/userdetails.html',{'form':fm})
    else:
        return redirect('login')
