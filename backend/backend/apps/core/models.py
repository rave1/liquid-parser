from django.db import models

# Create your models here.


class Liquid(models.Model):

    available = models.JSONField(default=list)
    picture = models.URLField(default=None)
    title = models.CharField(max_length=128)
