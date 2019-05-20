from django.conf.urls import include, url
from django.contrib import admin
from appdemo import views

urlpatterns = [
    url('genebook/', include('biodatabase.urls')),
    url(r'^$',views.index,name='index'),

    url(r'^register/$',views.register,name='register'),
    url(r'^register_commit/$',views.register_commit,name='register_commit'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_auth/$',views.login_auth,name='login_auth'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^upload_file/$',views.upload_file,name='upload_file'),

    url(r'^biodb_auth/$',views.biodb_auth,name='biodb_auth'),
    url(r'^gwasmed_auth/$',views.gwasmed_auth,name='gwasmed_auth'),
    url(r'^netpred_auth/$',views.netpred_auth,name='netpred_auth'),

    url(r'^admin/', admin.site.urls),
]
