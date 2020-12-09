from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)  #this class is an extension to the inbuilt User Model and this line says that the user object is Primary Key

    #additional objects besides the User model

    portfolio_site = models.URLField(blank= True)

    profile_pic = models.ImageField(blank= True , upload_to ='profile_pics')

    def __str__(self):
        return self.user.username


