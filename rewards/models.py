from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser

# Create your models here.

class Rewards(models.Model):
    code=models.CharField(max_length=30,null=True)
    discount=models.CharField(max_length=30,null=True,blank=True)
    bonus=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=130,null=True,blank=True)
    condition=models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return str(self.code)+ " " + str(self.description)
    

class UserRewards(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE,default=None)
    promocode=models.ForeignKey(Rewards,on_delete=models.CASCADE)

   
        



    