from django.urls import path
from django.conf.urls import include
from app.views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('about',about_us.as_view(),name='about'),
    path('blog',blog.as_view(),name='blog'),
    path('contact',contact.as_view(),name='contact'),
    path('portfolio',portfolio.as_view(),name='portfolio'),
    path('services',services.as_view(),name='services'),
    path('single_blog',single_blog.as_view(),name='single_blog'),
    path('prt1',prt1.as_view(),name='prt1'),
    
]