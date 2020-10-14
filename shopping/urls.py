from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^buy/', views.buyings, name='buying'),
    url(r'^seller/',views.sellings,name='selling'),
    url(r'^product/',views.productings,name='producting'),
    url(r'^contact/',views.contactings,name='contacting'),
    url(r'^search/',views.searchings,name='searching'),
    url(r'^getlist/',views.gettings,name='getting'),
    url(r'^contactlist/',views.contactings_detail,name='contacting_ul'),
    
    ]
