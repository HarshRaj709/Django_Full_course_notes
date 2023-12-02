from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'mysite/home.html')

def about(request):
    return render(request,'mysite/about.html')