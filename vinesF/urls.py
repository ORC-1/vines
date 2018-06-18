'''
Created on 26 Nov 2017

@author: ORC-1
'''
from django.conf.urls import include, url
from django.contrib import admin
from vinesF import views
import vinesF

#Generic View System
app_name ='vinesF'
urlpatterns = [
    url(r'^$', views.index, name='index'),
     
    
]