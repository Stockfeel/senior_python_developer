from django.db import models

# Create your models here.


class coffee(models.Model):
    name = models.TextField(max_length=20)
    bean_from = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
