from django.urls import path, include

from biodatabase import views

urlpatterns = [
    path('', views.genebook, name='genebook'),
    path('test/', views.ajax_dict, name='ajax-dict'),
    path('test2/', views.ajax_list, name='ajax-list'),
    path('search/', views.search, name='search'),
    path('searchm/', views.search_multi, name='searchm')
    #path('<int:blog_id>/', views.blogdetails, name='blogdetails' )
]