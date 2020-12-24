from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256,primary_key=True)
    principal = models.CharField(max_length=256)
    city = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=256)
    school = models.ForeignKey(School, on_delete = models.CASCADE,related_name='school')

    def __str__(self):
        return self.name
