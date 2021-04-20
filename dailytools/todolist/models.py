from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.

class ToDo(models.Model):
    date = models.DateField(auto_now=True)
    tasks = models.TextField()

    def __str__ (self):
        
        return str(self.date)