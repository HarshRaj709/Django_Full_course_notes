from django.shortcuts import render
from .models import Recipe,Ingridents

# Create your views here.
def home(request):
    Reci = Recipe.objects.all()
    ingri = Ingridents.objects.all()
    return render(request,'Dishes/home.html',{'rec':Reci,'ingr':ingri})

def recipe(request,id):
    reci = Recipe.objects.get(pk=id)
    return render(request,'Dishes/Dishes.html',{'recipe':reci})