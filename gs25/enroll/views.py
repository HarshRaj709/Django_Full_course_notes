from django.shortcuts import render
from .forms import userforms

# Create your views here.
def registration(request):
    #user = userforms(auto_id=False)
    user = userforms()
    user.order_fields(field_order=['First_name','names','email'])
    return render(request,'enroll/registration.html',{'use':user})