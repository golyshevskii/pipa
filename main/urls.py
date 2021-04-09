# импорт объекта admin для административной части веб-сайта и методов re_path, include для маршрутизации
# import of the admin object for the administrative part of the website and methods re_path, include for routing
from django.contrib import admin
from django.urls import re_path, include


# шаблоны маршрутизаторов
# router templates
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^account/', include('account.urls')),
]
