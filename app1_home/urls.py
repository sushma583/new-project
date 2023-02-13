from django.contrib import admin
from django.urls import path, re_path
from app1_home import views
from django.conf.urls import include

urlpatterns = [
    re_path(r'^$', views.welcome,name='welcome'),
]