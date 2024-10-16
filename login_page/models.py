from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile1(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name= models.CharField(max_length=200,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    last_name= models.CharField(max_length=200,null=True,blank=True)
    phone= models.CharField(max_length=200,null=True,blank=True)

    def _str_(self):
        return self.first_name
    
class prof(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name= models.CharField(max_length=200,null=True,blank=True)
    place = models.CharField(max_length=50,null=True,blank=True)
    last_name= models.CharField(max_length=200,null=True,blank=True)
    phone= models.CharField(max_length=200,null=True,blank=True)

    def _str_(self):
        return self.first_name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()