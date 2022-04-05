from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venue(models.Model):
    name =models.CharField(max_length=100)
    address =models.CharField(max_length=300)
    Zip_code =models.CharField('Zip Code', max_length=100)
    phone_number = models.CharField('Contact number',max_length=100 , blank =True)
    web = models.URLField('Website Address', blank = True)
    email_address = models.EmailField('Email address', blank = True)
    venue_image = models.ImageField(null = True , blank = True, upload_to = "images/")
    
    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class  Events(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue , blank = True , null = True , on_delete= models.CASCADE)
    #venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank = True, null =True , on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank = True )
    
    def __str__(self):
        return self.name
    
    