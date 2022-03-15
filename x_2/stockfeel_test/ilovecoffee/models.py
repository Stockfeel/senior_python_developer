from django.db import models

# Create your models here.
class Coffee(models.Model):
    name      = models.CharField(max_length=100, null=False)
    bean_from = models.CharField(max_length=100, null=False)
    price     = models.PositiveIntegerField(default=0)
