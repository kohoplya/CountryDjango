from django.db import models

class Country(models.Model):
    userName = models.CharField(max_length=255)
    telephone = models.IntegerField()
    countryName = models.CharField(max_length=255)
    capitalName = models.CharField(max_length=255)
    area = models.IntegerField()
    img = models.ImageField(upload_to='media/photos', blank=True, null=True)
    inputArea = models.CharField(max_length=255,)