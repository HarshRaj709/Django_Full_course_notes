from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fee_struct(request):
    fees = 2500
    return HttpResponse(f"your fees is {fees}")

def extra(response):
    return HttpResponse(f'if you want to learn frontend then your total fees will become = Rs.3550')