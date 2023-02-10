from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('about1',about_us.as_view(),name='about'),
    path('blog',blog.as_view(),name='blog'),
    path('contact',contact.as_view(),name='contact'),
    path('portfolio',portfolio.as_view(),name='portfolio'),
    path('services',services.as_view(),name='services'),
    path('single_blog',single_blog.as_view(),name='single_blog'),
    path('prt1',prt1.as_view(),name='prt1'),
    path('prt2',prt2.as_view(),name='prt2'),
    path('prt3',prt3.as_view(),name='prt3'),
    path('prt4',prt4.as_view(),name='prt4'),
    path('prt5',prt5.as_view(),name='prt5'),
    path('prt6',prt6.as_view(),name='prt6'),
    path('prt7',prt7.as_view(),name='prt7'),
    path('prt8',prt8.as_view(),name='prt8'),
    path('prt9',prt9.as_view(),name='prt9'),
    path('prt10',prt10.as_view(),name='prt10'),
    
]