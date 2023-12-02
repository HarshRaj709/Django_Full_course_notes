def middleware(get_response):
    print('1 time initialization')            #ye sirf ek bar chalega only line no.2
    def my_function(request):
        print('this will execute before the views.')#ye humara views ke chlne se phle chalega
        response = get_response(request)
        print('this will execute after the excution of views')      #ye views ke chlne ke bad chalega
        return response
    return my_function


class middleware:
    def __init__(self,get_response):
        self.get_response = get_response                #1 bar chlane wale ko init ke under likhte h.
        print('This will run only for 1 time.')

    def __call__(self,request):                             # jisko humko views se phle aur bad me chalana h usko hum call me likhte h
        print('This line will execute before the views')
        response = self.get_response(request)
        print('this will print after the views')
        return response