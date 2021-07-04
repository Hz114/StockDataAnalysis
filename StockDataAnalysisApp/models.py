from django.db import models

# Create your models here.


class MostActiveStock(models.Model):
    Symbols = models.CharField(max_length=10)
    Names = models.CharField(max_length=100)
    Prices = models.CharField(max_length=30)
    Changes = models.CharField(max_length=10)
    PercentageChanges= models.CharField(max_length=10)
    MarketCap = models.CharField(max_length=30)
    AverageVolume = models.CharField(max_length=30)
    Volume = models.CharField(max_length=30)

class GainerStock(models.Model):
    Symbols = models.CharField(max_length=10)
    Names = models.CharField(max_length=100)
    Prices = models.CharField(max_length=30)
    Changes = models.CharField(max_length=10)
    PercentageChanges = models.CharField(max_length=10)
    MarketCap = models.CharField(max_length=30)
    AverageVolume = models.CharField(max_length=30)
    Volume = models.CharField(max_length=30)

class LoserStock(models.Model):
    Symbols = models.CharField(max_length=10)
    Names = models.CharField(max_length=100)
    Prices = models.CharField(max_length=30)
    Changes = models.CharField(max_length=10)
    PercentageChanges = models.CharField(max_length=10)
    MarketCap = models.CharField(max_length=30)
    AverageVolume = models.CharField(max_length=30)
    Volume = models.CharField(max_length=30)