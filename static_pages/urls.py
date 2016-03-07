from django.conf.urls import include,url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$', views.index ,name='index'),
    url(r'^about/', views.about ,name='about'),
    url(r'^sidebar-left/', views.sidebar_left ,name='sidebar-left'),
    url(r'^sidebar-right/', views.sidebar_right ,name='sidebar-right'),

]