# импорт метода re_path для маршрутизации + импорт объектов представления относительно запросов из файла views
# import of the re_path method for routing + import of view objects relative to requests from the views file
from django.urls import re_path
from . import views
# импорт методов из объекта views для представления html шаблонов
# import methods from object views to view html templates
from django.contrib.auth import views as auth_views


app_name = 'account' 

# маршрутизаторы
# routers
urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    re_path(r'^$', views.profile, name='profile'),
    re_path(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    re_path(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html') , name='password_reset'),
    re_path(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
