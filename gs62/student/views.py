from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session.set_test_cookie()
    return render(request,'student/settestcookie.html')

def getsession(request):
    Correct=request.session.test_cookie_worked()
    return render(request,'student/gettestcookie.html',{'req':Correct})



def delsession(request):
    request.session.delete_test_cookie()
    return render(request,'student/deltestcookie.html')


def home(request):
    return render(request,'student/home.html')