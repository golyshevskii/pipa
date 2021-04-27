from django.urls import re_path
from . import views

app_name = 'board'

urlpatterns = [
    re_path(r'^profile-board/create/$', views.BoardCreate.as_view(), name='profile_board_create'),
    re_path(r'^profile-board/edit/$', views.BoardEdit.as_view(), name='profile_board_edit'),
    re_path(r'^profile-board/delete/$', views.BoardDelete.as_view(), name='profile_board_delete'),
    re_path(r'^$', views.Board.as_view(), name='profile_board')
]