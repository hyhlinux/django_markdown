# coding:utf-8
from django.conf.urls import url
from demo01 import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mark/$', views.mark, name='mark'),
]
