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
    path('LikeMeFast',like_me_fast.as_view(),name='prt1'),
    path('CoinHomes',CoinHomes.as_view(),name='prt2'),
    path('Pharsight',Pharsight.as_view(),name='prt3'),
    path('ShreeTextTile',ShreeTextTile.as_view(),name='prt4'),
    path('Instagram',Instagram.as_view(),name='prt5'),
    path('dyzner',dyzner.as_view(),name='prt6'),
    path('Hallour',Hallour.as_view(),name='Hallour'),
    path('domainmarket',domainmarket.as_view(),name='domainmarket'),
    path('YouTube',YouTube.as_view(),name='YouTube'),
    # path('prt7',prt7.as_view(),name='prt7'),
    # path('prt8',prt8.as_view(),name='prt8'),
    # path('prt9',prt9.as_view(),name='prt9'),
    # path('prt10',prt10.as_view(),name='prt10'),
    
]
handler404 = custom_404_view
