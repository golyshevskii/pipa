from django.urls import re_path
from . import views

app_name = 'chat'

urlpatterns = [
    re_path('^$', views.chat, name='chatroom')
]