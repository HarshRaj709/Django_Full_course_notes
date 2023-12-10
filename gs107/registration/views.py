from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# @login_required
def home(request):
    return render(request,'registration/home.html')

@login_required
def profile(request):
    return render(request,'registration/profile.html')

# @staff_member_required

def is_staff_member(user):
    return user.is_staff

@user_passes_test(is_staff_member,login_url='/normal_about/')       #here we check that if user is staffmember only then go to that function. 
def about(request):
    return render(request,'registration/about.html')        #isme agar humara login nhi h to admin login pr redirect krega.


def normal_about(request):
    return render(request,'registration/normal_about.html')