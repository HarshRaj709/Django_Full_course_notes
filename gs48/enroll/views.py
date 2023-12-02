from django.shortcuts import render
from .forms import UserForms

# Create your views here.
def home(request):
    if request.method =='POST':
        user = UserForms(request.POST)
        if user.is_valid():
            user.save()
    else:
        user = UserForms()
    return render(request,'enroll/home.html',{'use':user})