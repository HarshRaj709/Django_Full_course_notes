from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def home(request):
#     # mv=cache.get('movie',default='has_expired',)
#     # if mv == 'has_expired':
#     #     cache.set('movie','The one',30)
#     #     mv = cache.get('movie')
#     mv = cache.get_or_set('fees',45000,30,version = 2)
#     return render(request,'enroll/home.html',{'movie':mv})

# def home(request):
#     data = {'name':'hars','lname':'sahu'}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request,'enroll/home.html',{'stu':sv})

# def home(request):
#     cache.delete('fees',version=2)
#     return render(request,'enroll/home.html')


# def home(request):
#     cache.set('roll',101,30)
#     rv=cache.get('roll')
#     print(rv)
#     iv=cache.incr('roll',delta=5)
#     print(iv)
#     return render(request,'enroll/home.html')


def home(request):
    cache.clear()
    return render(request,'enroll/home.html')




