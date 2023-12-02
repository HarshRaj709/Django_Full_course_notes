from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
def home(request):
    return render(request,'caches/home.html')


def contact(request):         #iska cache nhi hua h to instant changes dekhne ko mil rha h.
    return render(request,'caches/contact.html')