from django.db import models

class coffee(models.Model):
    name = models.CharField(max_length=255)  
    bean_from = models.CharField(max_length=255)  
    price = models.IntegerField(max_length=20)  
