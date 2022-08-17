from django.db import models
import uuid

# Create your models here.

TOPIC_CHOICES = (
    ("Payment Status","Payment Status"),
    ("My Order","My Order"),
    ("Returns","Returns"),
    ("Cancellation","Cancellation"),
    ("Shipping Status","Shipping Status"),
    ("General Information","General Information"),
    ("Other","Other"),
    
)
    
class Inquerer(models.Model):
    inqueryNo=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    companyOrganization=models.CharField(max_length=30,null=True)
    phoneNumber=models.CharField(max_length=30,null=True)
    additionalInfo=models.CharField(max_length=30,null=True)

   
    def __str__(self):
        return str(self.firstName )+ " " + str(self.lastName )+ " " + str(self.email )
   
class Devices(models.Model):
    inquerer=models.ForeignKey(Inquerer, related_name='devices', on_delete=models.CASCADE)
    deviceOrder=models.IntegerField(blank=True,null=True)
    deviceType=models.CharField(max_length=30,null=True)
    deviceCondition=models.CharField(max_length=30,null=True)
    deviceQuantity=models.IntegerField(blank=True,null=True)
        
class GeneralInquery(models.Model):
    caseNo=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=30,null=True)
    topic=models.CharField(choices= TOPIC_CHOICES,max_length=30,null=True)
    subject=models.CharField(max_length=300,null=True)
    description=models.CharField(max_length=2000,null=True)

    

