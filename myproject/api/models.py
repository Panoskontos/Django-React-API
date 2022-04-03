from django.db import models

# Create your models here.
class Product(models.Model):
    # id 
    name = models.CharField(max_length=70, blank=True)
    description = models.TextField(max_length=200)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Movie(models.Model):
    # id 
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=200)
    starring = models.CharField(max_length=350)

    def __str__(self):
        return self.name
