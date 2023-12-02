from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Harsh'
    request.session['lname'] = 'sahu'
    return render(request,'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    # Alternate Way
    name = request.session.get('name',default='guestx')   #same as cookie here we get guestx if our session not already created//store.
    lname = request.session.get('lname',default='guest ki cast')
    return render(request,'student/getsession.html',{'name':name,'lname':lname})

def deletesession(request):
    if 'name' in request.session:
        # present = 'session contains name'
        del request.session['name']
        del request.session['lname']
    return render(request,'student/delsession.html')  # our data is deleted but session is showing at browser


def home(request):
    return render(request,'student/home.html')




                    # #We can Add Multiple Data in 1 session # #