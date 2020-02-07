
from django.urls import path, include
from apps.board.views import (PostCreateView,
    PostCreateViewNew,
                                     PostDeleteView,
                                     PostDetailView,
                                     # PostListView,
                                     PostSearchView,
                                     PostUpdateView)


app_name = 'board'
urlpatterns = [
    path('', PostSearchView.as_view(), name='list'),
    path('new/', PostCreateViewNew.as_view(), name='createnew'),
    path('posts/', PostSearchView.as_view(), name='list'),
    path('posts/new/', PostCreateView.as_view(), name='create'),
    path('posts/(?P<slug>[-\w]+)/edit/', PostUpdateView.as_view(), name='update'),
    path('posts/(?P<slug>[-\w]+)/delete/', PostDeleteView.as_view(), name='delete'),
    path('posts/(?P<slug>[-\w]+)/', PostDetailView.as_view(), name='detail'),
]
