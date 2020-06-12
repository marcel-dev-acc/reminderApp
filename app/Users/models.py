from django.db import models

# Create your models here.
class AppUser(models.Model):
    Username = models.CharField(max_length=25,blank=False)
    Password = models.CharField(max_length=25,blank=False)
    Fname = models.CharField(max_length=100,blank=False)
    Lname = models.CharField(max_length=100,blank=False)
    PhoneNumber = models.CharField(max_length=50,blank=False)
    IsAdmin = models.BooleanField(default=False,blank=False)