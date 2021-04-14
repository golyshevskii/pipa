from django.contrib import admin
# импорт модели Profile, для добавления полей на страницу администрации сайта
# import of the Profile model, to add fields to the site administration page
from .models import Profile 


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


admin.site.register(Profile, ProfileAdmin)
