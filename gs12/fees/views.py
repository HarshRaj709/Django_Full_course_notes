from django.shortcuts import render

# Create your views here.
def fees(request):
    list = [1200,1300,1500,2500]
    return render(request,'fees/fees_home.html',{'lis':list})