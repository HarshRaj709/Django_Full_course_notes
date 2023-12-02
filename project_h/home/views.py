from django.shortcuts import render
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1':'hola ka gola',
        'variable2':'mera naam koyla',
        'active':'active'
    }
    return render(request,'home/home.html',context)

def about(request):
    active = {'act':'active'}
    return render(request,'home/about.html',active)

def services(request):
    return render(request,'home/services.html')

def contact(request):
    nav = {'actnav':'active'}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name,email = email,message=message)  #date = datetime.today()
        # if contact.is_valid():              # yha pe hum valid function ko use nhi kr sakte h kyoki wo only forms ke sath hi kaam krta h.
        contact.save()
        messages.success(request,'Thanks to contact us ...')
    return render(request,'home/contact.html',nav)