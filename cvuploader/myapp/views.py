from django.shortcuts import render,redirect
from .forms import ResumeForm
from django.contrib import messages
from .models import Resume

# Create your views here.
def home(request):
    profile = Resume.objects.all()
    if request.method == 'POST':
        fm = ResumeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thanks to Upload Your resume')
            return redirect('home')
    else:
        fm = ResumeForm()
    return render(request,'myapp/home.html',{'form':fm,'pro':profile})


def candidate(request,pk):
    fm = Resume.objects.get(pk=pk)
    return render(request,'myapp/profile.html',{'form':fm})