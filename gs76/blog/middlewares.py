from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_view(self,request,*args,**kwargs):
        print('THis is process view before view')
        #return HttpResponse('THis is before view')           #agar isko hum comment krde to humara views chal jayega.
        return None
    


class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_exception(self,request,exception):
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        print('THis is process view before view')
        #return HttpResponse('THis is before view')           #agar isko hum comment krde to humara views chal jayega.
        return HttpResponse(msg)
    

class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        print('1 bar chalega yaar')
        self.get_response = get_response
    
    def __call__(self,request):
        print('print before our views function')
        response = self.get_response(request)
        print('this will run after the views')
        return response
    
    def process_template_response(self,request,response):
        print('process template response from MIDDLEWARE')
        response.context_data['name'] = 'Rahul'         #used to change data which we get from views
        return response
