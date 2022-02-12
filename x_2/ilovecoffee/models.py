
from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    bean_from = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
