from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    name=request.session['name'] ='harsh'
    request.session.set_expiry(10)
    # request.session.set_expiry(0)  #----> This will make session expire after browser get closed.
    return render(request,'student/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name=request.session.get('name',default='guest')
        request.session.modified = True                                #iske wajah se refresh ho ja rha h humare refresh krne se
        return render(request,'student/getsession.html',{'name':name})
    else:
        return HttpResponse('Your Session is expired')



def delsession(request):
    if 'name' in request.session:
        request.session.flush()
        request.session.clear_expired()    #This will make our Database clean..
    return render(request,'student/delsession.html')


def home(request):
    return render(request,'student/home.html')