from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class usermodel(AbstractBaseUser):
    username=models.CharField(max_length=20,blank=False,unique=True)
    email=models.CharField(max_length=40,blank=False)
    access=models.CharField(max_length=5,blank=False,default='user')

    USERNAME_FIELD='username'

class concertmodel(models.Model):
    concertname=models.CharField(max_length=20)
    concertdate=models.DateField()
    concerttime=models.TimeField()
    concertvenue=models.CharField(max_length=20)
    ticketprice=models.DecimalField(max_digits=10,decimal_places=2)
    availabletickets=models.IntegerField()

class ticketbooking(models.Model):          
    concertname=models.CharField(max_length=20)
    ticketprice=models.DecimalField(max_digits=12,decimal_places=2)
    username=models.CharField(max_length=20)
    useremail=models.CharField(max_length=40)
    bookedtickets=models.IntegerField()
    totalprice=models.DecimalField(max_digits=12,decimal_places=2)