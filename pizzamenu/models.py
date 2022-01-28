from django.db import models

# Create your models here.
class Pizzamenu(models.Model):
 name = models.CharField(max_length=255)
 price = models.FloatField()
 image = models.CharField(max_length=255)