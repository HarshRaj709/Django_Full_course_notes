from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
# def home(request):
#     all_post = Post.objects.all().order_by('title')             #without order ke ye 'unordered object_list: <class 'blog.models.Post'> QuerySet' error dega.
#     items_per_page = 3
#     paginator = Paginator(all_post,items_per_page)
#     page_number = request.GET.get('page')        #fetching page number from created page.
#     page_obj = paginator.get_page(page_number)      #isse hum uss page per pahuch jayege
#     print(paginator)
#     print()
#     print(page_number)
#     print()
#     print(page_obj)
#     return render(request,'blog/home.html',{'posts':page_obj})

def home(request):
    all_post = Post.objects.all().order_by('title')             #without order ke ye 'unordered object_list: <class 'blog.models.Post'> QuerySet' error dega.
    items_per_page = 3
    paginator = Paginator(all_post,items_per_page,orphans = 2)      #isse humare last ke 2 posts bhi uske previous post page me adjust ho jayega.
    page_number = request.GET.get('page')        #fetching page number from created page.
    page_obj = paginator.get_page(page_number)      #isse hum uss page per pahuch jayege
    print(paginator)
    print()
    print(page_number)
    print()
    print(page_obj)
    return render(request,'blog/home.html',{'posts':page_obj})