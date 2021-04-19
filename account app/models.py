from django.db import models
# импорт класса AbstractUser для унаследования полей ифнормации о пользователе
# import of AbstractUser class to inherit user info fields
from django.contrib.auth.models import AbstractUser


# модель Profile, для хранения информации о пользователе
# the Profile model, for storing information about the user
class Profile(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Activated')
    send_messages = models.BooleanField(default=True, verbose_name='Comment Notifications')
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    # опции класса
    # class options
    class Meta(AbstractUser.Meta):
        pass

    # строковое представление модели
    # string representation of the model
    def __str__(self):
        return self.username
