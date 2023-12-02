from django.shortcuts import render

# Create your views here.
def counter(request):
    ct = request.session.get('count',default=0)
    addcount = ct +1
    request.session['count'] = addcount
    request.session.set_expiry(0)
    return render(request,'counter/home.html',{'add':addcount})