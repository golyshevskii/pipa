# импорт метода re_path для маршрутизации + импорт объектов представления относительно запросов из файла views
# import of the re_path method for routing + import of view objects relative to requests from the views file
from django.urls import re_path
from . import views

# определение названия приложения
# define the name of the application
app_name = 'account' 

# шаблоны маршрутизаторов
# router templates
urlpatterns = [
    re_path(r'^login/$', views.user_login, name='login')
]
