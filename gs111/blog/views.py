from typing import Any
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import Http404


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['title']
    paginate_by = 3         #btyega ki kitne aane chaiye 1 page me   ----- important
    paginate_orphans = 2        #last ke 2 bhi uske previous page me aagye.

    #isme problem h ki humare extra page number dalne pr 404error de rha h. usko sahi krne ke liye..
    def get_context_data(self, **kwargs):
        try:
            return super(Home,self).get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(Home,self).get_context_data(**kwargs)



    # context_object_name = 'posts'