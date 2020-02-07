from django.urls import path, include, re_path
from news.views import *

urlpatterns = [
    re_path(r'^showNews/$',showNews,name='showNews'),
    re_path(r'^news/(?P<id>\d+)/$',showOne,name='showOne')
]