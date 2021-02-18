from django.db import models


# Create your models here


class User_part(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    email = models.CharField(max_length=30) 
    password1 = models.CharField(max_length=30) 
    password2 = models.CharField(max_length=30) 
    status_choices = models.CharField(max_length=30)
    

    def __str__(self):
        return self.first_name

class Admin_part(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    email = models.CharField(max_length=30) 
    password1 = models.CharField(max_length=30) 

    def __str__(self):
        return self.first_name
       


