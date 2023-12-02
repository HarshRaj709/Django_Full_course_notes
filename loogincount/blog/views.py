from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Post
from .forms import SignupForm,LoginForm,PostForm
from django.contrib.auth.models import Group
from django.core.cache import cache

# Create your views here.

#home
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts,'activate':'active'})

def about(request):
    return render(request,'blog/about.html',{'about':'active'})

def contact(request):
    return render(request,'blog/contact.html',{'contact':'active'})

def Dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()
        ip = request.session.get('ip',default=0)
        ct = cache.get('count',version = user.pk)
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':groups,'dashboard':'active','ip':ip,'ct':ct})
    else:
        return redirect('login')

def User_Logout(request):
    logout(request)
    # messages.success(request,'Author Signed Out successfully')
    return redirect('home')

def Signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request,'Congratulations !! You become a Author ')
    else:
        fm = SignupForm()
    return render(request,'blog/signup.html',{'form':fm,'signup':'active'})

def User_Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname,password = upass)
                if user is not None:
                    login(request,user)
                    if user.is_superuser:
                        messages.success(request,'Admin loginned successfully')
                    else:
                        messages.success(request,'Author loginned successfully')
                    return redirect('dashboard')
        else:
            fm = LoginForm()
        return render(request,'blog/login.html',{'form':fm,'login':'active'})
    else:
        return redirect('dashboard')
    

#Post delete
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.success(request,'POST Deleted Successfully --  '+ str(pi))
            return redirect('dashboard')
    else:
        return redirect('login')

def update_post(request,id):
    pi = Post.objects.get(pk=id)
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PostForm(request.POST,instance = pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Post Updated Successfully!!  '+ str(pi))
                return redirect('dashboard')
        else:
            fm = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':fm})
    else:
        return redirect('login')

def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PostForm(request.POST)   #yha pe humne Postform ko phle bnya h taki hum usko render kr sake tabhi to edit ho payega
            if fm.is_valid():
                fm.save()
                fm = PostForm()
                messages.success(request,'Post Added Successfully!!')
                return redirect('dashboard')
        else:
            fm = PostForm()
            return render(request,'blog/addpost.html',{'form':fm})
    else:
        return redirect('login')