from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView

# Create your views here.
class StudentListView(ListView):
    model = Student         #humko isise sara objects mil gya default context object me .... object_list
    # by default humare template ka naam hona chahiye---'school/student_list.html',,,,folder/modelname_list.html
    # by default humare sare models ke objects store hue h student_list naam ke context me..
