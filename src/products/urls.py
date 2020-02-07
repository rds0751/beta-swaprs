from django.conf import settings
from django.conf.urls import include, url, re_path

from django.contrib import admin
from .views import *
admin.autodiscover()

urlpatterns = [
    re_path(r'^$', list_all, name="all_products"),
    re_path(r'^search/', search, name="search"),
    re_path(r'^add/', add_product, name="add_product"),
    re_path(r'^(?P<slug>.*)/edit/', edit_product, name="edit_product"),
    re_path(r'^add_wish/', add_wish, name="add_wish"),
    re_path(r'^(?P<slug>.*)/edit/', edit_wish, name="edit_wish"),
    re_path(r'^category/(?P<slug>.*)/$', category_single, name="category"),
    re_path(r'^(?P<slug>.*)/download/(?P<filename>.*)', download_product, name='download_product'),
    re_path(r'^(?P<slug>.*)/$', single, name="single_product"),
]