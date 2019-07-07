from django.conf.urls import url
from .views import index, room
from . import views
from django.urls import path, re_path

app_name = 'chat'

urlpatterns = [
    path(r'^$', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
