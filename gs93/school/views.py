from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import ContactForm

# Create your views here.
def homefun(request):
    return render(request,'school/home.html')


class Myhome(View):
    def get(self,request):          #jab bhi hum koi rquest krte h to get method ke through aata h.
        return render(request,'school/class.html')
    
def about(request):
    context = {'msg':'Function Based views'}
    return render(request,'school/about.html',context)

class About(View):
    def get(self,request):
        context = {'msg':'Class Based views'}
        return render(request,'school/about.html',context)
    

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thankyou Form submitted')
        
    else:
        form = ContactForm()
    return render(request,'school/contact.html',{'form':form})


class Contact(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'school/contact.html',{'form':form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thankyou Form submitted')
        
# def news(request):
#     template = 'school/news.html'
#     context={'info':'Earning money is important to sustain.'}
#     return render(request,template,context)


def news(request,template):         #passing templates through urls.py
    # template = 'school/news.html'
    context={'info':'Earning money is important to sustain.'}
    return render(request,template,context)


# class News(View):
#     template = 'school/news.html'
#     def get(self,request):
#         context={'info':'Earning money is important to sustain.'}
#         return render(request,self.template,context)

class News(View):
    template = ''
    def get(self,request):
        context={'info':'Earning money is important to sustain.'}
        return render(request,self.template,context)
    
