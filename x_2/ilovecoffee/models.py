from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    bean_from = models.CharField(max_length=20)
    price = models.IntegerField()