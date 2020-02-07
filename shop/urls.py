from django.urls import path, include, re_path
from shop.views import *
urlpatterns = [
    re_path(r'^delete_product/(?P<product_id>\d+)/',delete_product,name='delete_product'),
    re_path(r'^add_product/',add_product,{'product_id':None},name='add_product'),
    re_path(r'^addProductFromTB/',addProductFromTB,name='addProductFromTB'),
    re_path(r'^orders/', show_shop_orders,name='show_my_orders'),
    re_path(r'^edit_product/(?P<product_id>\d+)/',add_product,name='edit_product'),
    re_path(r'^get_categories/',get_categories, ({'categories':None}),name='get_categories'),
    re_path(r'^get_categories/(.*)/',get_categories,name='get_category'),
    re_path(r'^capture_tmp/',capture_tmp),
    re_path(r'^', show_products, name='show'),
    re_path(r'^change/(?P<cart_id>\d+)/(?P<value>\d+|\d+.\d+|\w+)/(?P<type>\w+)/', change, name='change'),
    re_path(r'^upload_track_code/(?P<order_id>\d+)/', upload_track_code,name='upload_track_code'),
    re_path(r'^contacts/',contacts,name='contact'),
    re_path(r'^action/',action,name='action'),
#    re_path(r'^setTrust/(?P<trust>\w+)/',setTrust,name='setTrust')
]