from django.db import models
from django.utils import timezone

# Create your models here.

class StoreLocation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class HomeLocation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    storelocation = models.ForeignKey(StoreLocation)
    homelocation = models.ForeignKey(HomeLocation)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
