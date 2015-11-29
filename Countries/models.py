from django.db import models

class Country(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=4)


class City(models.Model):
    Country = models.ForeignKey(Country)
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=4)
    Population = models.DecimalField(max_digits=15, decimal_places=2)


class Language(models.Model):
    Country = models.ForeignKey(Country)
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=4)

# Create your models here.
