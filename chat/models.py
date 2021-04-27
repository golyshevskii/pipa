from django.db import models


# определение базы данных сообщений
# defining the message database
class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.TextField(null=True, blank=True)
