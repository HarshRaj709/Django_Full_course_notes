from django.shortcuts import render

# Create your views here.
def setsession(request):
    name=request.session['name'] ='harsh'
    request.session.set_expiry(10)
    request.session.set_expiry(0)  #----> This will make session expire after browser get closed.
    return render(request,'student/setsession.html')

def getsession(request):
    name=request.session.get('name',default='guest')
    ages = request.session.get_session_cookie_age()    #ages = request.session.get_session_cookie_age--> So, if you use it like this, ages will not contain the session age but will instead contain a reference to the method.
    age = ages/(60*60*24)
    real_age = request.session.get_expiry_age()
    expiry = request.session.get_expiry_date()
    # exp = expiry/(60*60*24)
    browser = request.session.get_expire_at_browser_close()
    return render(request,'student/getsession.html',{'name':name,'age':age,'exp':expiry,'bro':browser,'real':real_age})



def delsession(request):
    if 'name' in request.session:
        request.session.flush()
        request.session.clear_expired()    #This will make our Database clean..
    return render(request,'student/delsession.html')


def home(request):
    return render(request,'student/home.html')