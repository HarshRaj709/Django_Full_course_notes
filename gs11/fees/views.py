from django.shortcuts import render

# Create your views here.
def fee(request):
    dict = {'fees':7500}
    return render(request,'fees/fees_home.html',dict)