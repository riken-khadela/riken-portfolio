from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('project/<slug:slug>', project_detail, name='project_detail'),
    path('project',project_list.as_view(),name='ProjectList'),
    path('',Home.as_view(),name='home'),
    path('about',about_us.as_view(),name='about'),
    path('blog',blog.as_view(),name='blog'),
    path('contact',contact.as_view(),name='contact'),
    path('portfolio',portfolio.as_view(),name='portfolio'),
    path('services',services.as_view(),name='services'),
    path('single_blog',single_blog.as_view(),name='SingleBlog'),
    path('LikeMeFast',prt1.as_view(),name='prt1'),
    path('CoinHomes',prt2.as_view(),name='prt2'),
    path('TeleGramBot',prt3.as_view(),name='prt3'),
    path('ShreeTextTile',prt4.as_view(),name='prt4'),
    path('Instagram',prt5.as_view(),name='prt5'),
    path('dyzner',prt6.as_view(),name='prt6'),
    # path('prt7',prt7.as_view(),name='prt7'),
    # path('prt8',prt8.as_view(),name='prt8'),
    # path('prt9',prt9.as_view(),name='prt9'),
    # path('prt10',prt10.as_view(),name='prt10'),
    
]