from django.shortcuts import render

# Create your views here.

def show_details(request,year):
    student = {'yr':year}
    return render(request,'enroll/show.html',student)
