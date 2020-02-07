from django.urls import path, include
from log.views import *
urlpatterns = [
    path('wall_more/',wall_more,name='wall_more'),
]