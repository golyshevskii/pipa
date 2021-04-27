from django.db import models


class ProfileBoard(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    url = models.URLField(max_length=200)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
