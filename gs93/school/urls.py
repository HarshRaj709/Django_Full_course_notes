from django.urls import path
from . import views

urlpatterns = [
    path('',views.homefun,name='home'),
    path('cl/',views.Myhome.as_view(),name='class'),         #humko yha pe function chaiy hota h but hum yha class de rhe h to usko sahi krne ke liy .as_view() use hota h.
    path('about/',views.about,name='about'),
    path('abcl/',views.About.as_view(),name='abclass'),
    path('form/',views.contact,name='contact'),
    path('clform/',views.Contact.as_view(),name='clform'),
    # path('news/',views.news,name='name')
    path('news/',views.news,{'template':'school/news.html'},name='name'),   #passing templates through urls
    # path('newscl/',views.News.as_view(),name='clnews')
    path('newscl/',views.News.as_view(template = 'school/news.html'),name='clnews'),
    
]
