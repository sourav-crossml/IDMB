from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name= 'Home'
urlpatterns =[
    path('',views.index,name='index'),
    path('artist',views.artist,name='artist'),
    path('award',views.award,name='award'),
    path('rating',views.rating,name='rating'),
    path('topten/', views.topten, name ='topten'),
    path('leastten/', views.leastten, name ='leastten'),
    path('within/', views.within, name ='within'),
    path('search/', views.search_results, name='search_results'),

]