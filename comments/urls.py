from django.urls import path, include, re_path

from comments.views import *

urlpatterns = [
    re_path(r'^post_comment/(?P<id>\d+)/$',post_comment,name='post_comment'),


    re_path(r'^show_chat/(?P<to>\w+)/$',show_chat,name='send_message'),
    re_path(r'^post_message/(?P<to>\w+)/$',post_message,name='post_message'),

    path('show_messages/',show_messages,name='show_messages'),
]