# импорт метода models
from django.db import models
# импорт класса AbstractUser для унаследования полей ифнормации о пользователе
from django.contrib.auth.models import AbstractUser


# модель Profile, для хранения информации о пользователе
class Profile(AbstractUser):
    # поле активации пользователя
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Activated')
    send_messages = models.BooleanField(default=True, verbose_name='Comment Notifications')
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    # опции класса
    class Meta(AbstractUser.Meta):
        pass

    # строковое представление модели
    def __str__(self):
        return self.username
