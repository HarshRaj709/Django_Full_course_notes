from django.shortcuts import render

# Create your views here.
def fees(request):
    return render(request,'fees/fees_home.html')