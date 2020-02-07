from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('on-boarding/',views.about,name ='about'),
    path('profiles/start-swapping/',views.start,name ='about'),
    path('profiles/',views.profile,name ='about'),
    path('profiles/settings/',views.settings,name ='about'),
    path('add-wish/',views.add_wish,name ='about'),
    path('edit item/',views.edit_item,name ='about'),
    path('edit-wish/',views.edit_wish,name ='about'),
]
