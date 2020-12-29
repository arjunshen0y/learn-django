from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50,default='lol')

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name



