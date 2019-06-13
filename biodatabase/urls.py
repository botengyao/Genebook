from django.urls import path, include
from biodatabase import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.genebook, name='genebook'),
    path('search/', views.search, name='search'),
    path('searchmulti/', views.search_multi, name='searchmulti'),
    path('search/downloads', views.downloads, name='downloads'),
    path('search/download', views.download, name='download')
    #path('<int:blog_id>/', views.blogdetails, name='blogdetails' )
]