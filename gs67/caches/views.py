from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(20)  #isko krne ke bad caches ka kaam nhi krna pdta h settings.py me ye easy aur convenient h. Table nhi bni h but chal rha h sahi.
def home(request):
    return render(request,'caches/home.html')

@cache_page(30)
def contact(request):         #iska cache nhi hua h to instant changes dekhne ko mil rha h.
    return render(request,'caches/contact.html')