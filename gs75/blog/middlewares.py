# def middleware(get_response):
#     print('1 time initialization')            #ye sirf ek bar chalega only line no.2
#     def my_function(request):
#         print('this will execute before the views.')#ye humara views ke chlne se phle chalega
#         response = get_response(request)
#         print('this will execute after the excution of views')      #ye views ke chlne ke bad chalega
#         return response
#     return my_function
from django.shortcuts import HttpResponse

class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response                #1 bar chlane wale ko init ke under likhte h.
        print('This is Brother Middleware.')

    def __call__(self,request):                             # jisko humko views se phle aur bad me chalana h usko hum call me likhte h
        print('This Brother line will execute before the views')
        response = self.get_response(request)
        print('this Brother will print after the views')
        return response
    

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response                #1 bar chlane wale ko init ke under likhte h.
        print('This is Father Middleware.')

    def __call__(self,request):                             # jisko humko views se phle aur bad me chalana h usko hum call me likhte h
        print('This Father line will execute before the views')
        #response = self.get_response(request)   #get_response likhne ka matlab h ki wo father ke pass jayega means ki next middleware ke pass jayega.
        response = HttpResponse('nikal lo')         #esse ye next middleware ke pass na jkr humare targeted location pe jayega.
        print('this Father will print after the views')
        return response
    

class MummyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response                #1 bar chlane wale ko init ke under likhte h.
        print('This is Mummy Middleware.')

    def __call__(self,request):                             # jisko humko views se phle aur bad me chalana h usko hum call me likhte h
        print('This Mummy line will execute before the views')
        response = self.get_response(request)
        print('this Mummy will print after the views')
        return response