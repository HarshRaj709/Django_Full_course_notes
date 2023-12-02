from django.shortcuts import render

# Create your views here.
def home(request,check):
    return render(request,'enroll/home.html',{'check':check})

# def show_details(request,my_id):
#     print(my_id)
#     return render(request,'enroll/show.html',{'id':my_id})

def show_details(request,my_id=1):
    if my_id==1:   #isko str kro ya dyanamic url ko integer krdo, to humne usko int krdiya h.
        student={'id':my_id,'name':'Harsh'}
    if my_id==2:
        student={'id':my_id,'name':'Ashish'}
    if my_id==3:
         student={'id':my_id,'name':'Akshay'}
    if my_id==4:
        student={'id':my_id,'name':'Burnol'}
    return render(request,'enroll/show.html',student)


def show_subdetails(request,my_id,my_subid):
    if my_id==1 and my_subid==1:   #isko str kro ya dyanamic url ko integer krdo, to humne usko int krdiya h.
        student={'id':my_id,'name':'Harsh sub','info':'Sub-details'}
    if my_id==2 and my_subid==2:
        student={'id':my_id,'name':'Ashish sub','info':'Sub-details'}
    if my_id==3 and my_subid==3:
         student={'id':my_id,'name':'Akshay sub','info':'Sub-details'}
    if my_id==4 and my_subid==4:
        student={'id':my_id,'name':'Burnol sub','info':'Sub-details'}
    return render(request,'enroll/show.html',student)