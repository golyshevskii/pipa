# импорт метода re_path для маршрутизации + импорт объектов представления относительно запросов из файла views
# import of the re_path method for routing + import of view objects relative to requests from the views file
from django.urls import re_path
from . import views
# импорт методов LoginView + LogoutView для представления шаблонов login.html + logout.html
# import LoginView + LogoutView methods to view templates login.html + logout.html
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'account' 

# шаблоны маршрутизаторов
# router templates
urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    re_path(r'^$', views.profile, name='profile'),
]
