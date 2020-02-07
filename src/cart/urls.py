from django.conf import settings
from django.conf.urls import re_path, include, url

from django.contrib import admin
from .views import *
admin.autodiscover()

urlpatterns = [
    re_path(r'^$', cart, name="cart"),
    re_path(r'^update_cart/(?P<id>.*)', update_cart, name="update_cart"),

]
