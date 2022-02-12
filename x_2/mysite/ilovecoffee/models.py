from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=200)
    bean_from = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=0)
