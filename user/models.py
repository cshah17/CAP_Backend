from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
# Create your models here.
STATUS_CHOICES=(
    ('completed','completed'),
    ('In-Progress','In-Progress')
)
DEVICE_REVIEW_CHOICES=(
    ('Ok','ok' ),
    ('Requoted','Requoted'),
)
PAYMENT_CHOICES=(
    ('Venmo','Venmo' ),
    ('Paypal','Paypal' ),
    ('Zelle','Zelle' ),
    ('CashApp','CashApp'),
 )
SHIPPING_CHOICES=(
    ('local-pickup','local-pickup' ),
    ('USPS','USPS' ),
    ('FedEx', 'FedEx' ),
    ('UPS','UPS' ),
 )
ACCEPTANCE_CHOICES=(
    ('yes','yes' ),
    ('Customer Denied','Customer Denied' ),
    ('No', 'No' ),
    ('Other','Other' ),
 )

    #Auth User model
class UserInfo(models.Model):
    user=models.ForeignKey('auth.User', related_name='userinfo', on_delete=models.CASCADE)
    secondary_email=models.EmailField(blank=True,null=True)
    phoneNumber=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return str(self.user) 

class UserAddress(models.Model):
    user=models.ForeignKey('auth.User', related_name='useraddress', on_delete=models.CASCADE)
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    addressType=models.CharField(max_length=30,null=True)
    addressLine1=models.CharField(max_length=30,null=True)
    addressLine2=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    zipcode=models.CharField(max_length=30,null=True)
    primaryAddress=models.BooleanField(default=False,null=True)


    def __str__(self):
        return str(self.user)+ " " +str(self.addressType)+ " " +str(self.addressLine1)+ " " +str(self.addressLine2)+ " "+str(self.city)+ " "+str(self.state)+ " "+str(self.zipcode)+ " "+str(self.primaryAddress)

class UserPaymentInfo(models.Model):
    user=models.ForeignKey('auth.User',related_name='userpaymentmethod',on_delete=models.CASCADE)
    paymentMethod=models.CharField(choices=PAYMENT_CHOICES,max_length=30,null=True,blank=True)
    name=models.CharField(max_length=30,blank=True,null=True)
    username=models.CharField(max_length=30,blank=True,null=True)
    Phone=models.CharField(max_length=30,blank=True,null=True)
    email=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return str(self.user)+ " " +str(self.paymentMethod)+ " " +str(self.username)
'''class UserOrder(models.Model):
    user=models.ForeignKey('auth.User', related_name='userorder', on_delete=models.CASCADE)

    def __str__(self):
        return (self.user.username) '''

class UserTradeInfo(models.Model):
    user=user=models.ForeignKey('auth.User', related_name='userorder', on_delete=models.CASCADE,default=1)
    orderNo=models.UUIDField(default=uuid.uuid4, editable=False)
    status=models.CharField(choices=STATUS_CHOICES,max_length=30,null=True)
    address=models.ForeignKey(UserAddress,related_name='orderaddress',on_delete=models.CASCADE, null=True, blank=True)
    orderDate=models.DateTimeField(auto_now=True)
    lableSent=models.DateField(null=True,blank=True)
    shippingLableReceived=models.DateField(null=True,blank=True)
    deviceReceived=models.DateField(null=True,blank=True)
    deviceReview=models.CharField(choices=DEVICE_REVIEW_CHOICES,max_length=30,null=True,default=None,blank=True)
    deviceAccepted=models.CharField(choices=ACCEPTANCE_CHOICES,max_length=30,null=True,default=None,blank=True)
    deviceAcceptanceComment=models.CharField(max_length=300,blank=True,null=True)
    totalPayment=models.CharField(max_length=30,blank=True,null=True)
    paymentMethod=models.ForeignKey(UserPaymentInfo,related_name='paymentmethod',on_delete=models.CASCADE, null=True, blank=True)
    paymentReferenceNo=models.CharField(max_length=30,blank=True,null=True)
    deviceShippingMethod=models.CharField(choices=SHIPPING_CHOICES,max_length=30,null=True)
    deviceTrackingInbound=models.CharField(max_length=30,blank=True,null=True)
    deviceTrackingOutbound=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return str(self.orderNo)+ " " +str(self.user)

class UserDevicesInfo(models.Model):
    
    trade=models.ForeignKey(UserTradeInfo,related_name='devices',on_delete=models.CASCADE)
    deviceNo=models.CharField(max_length=30,blank=True,null=True)
    deviceType=models.CharField(max_length=30,blank=True,null=True)
    deviceModel=models.CharField(max_length=30,blank=True,null=True)
    deviceSerial=models.CharField(max_length=30,blank=True,null=True)
    deviceImei=models.CharField(max_length=30,blank=True,null=True)
    deviceImei2=models.CharField(max_length=30,blank=True,null=True)
    deviceMacAddress=models.CharField(max_length=30,blank=True,null=True)
    deviceCapacity=models.CharField(max_length=30,blank=True,null=True)
    deviceCarrier=models.CharField(max_length=30,blank=True,null=True)
    deviceCondition=models.CharField(max_length=30,blank=True,null=True)
    deviceYear=models.CharField(max_length=30,blank=True,null=True)
    deviceProcessor=models.CharField(max_length=30,blank=True,null=True)
    deviceOffer=models.CharField(max_length=30,blank=True,null=True)
    deviceGeneration=models.CharField(max_length=30,blank=True,null=True)
    deviceSize=models.CharField(max_length=30,blank=True,null=True)
    deviceEdition=models.CharField(max_length=30,blank=True,null=True)
    deviceBand=models.CharField(max_length=30,blank=True,null=True)
    deviceEngraving=models.CharField(max_length=30,blank=True,null=True)
    #deviceImages=models.ImageField(upload_to='Deviceimg',blank=True,null=True)
    
    #Guest user models



    #Guest user models
class GuestUserTradeInfo(models.Model):
    firstName=models.CharField(max_length=30,null=True)
    lastName=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    companyOrganization=models.CharField(max_length=30,null=True)
    phoneNumber=models.CharField(max_length=30,null=True)
    addressType=models.CharField(max_length=30,null=True)
    addressLine1=models.CharField(max_length=30,null=True)
    addressLine2=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    zipcode=models.CharField(max_length=30,null=True)
    orderNo=models.UUIDField(default=uuid.uuid4, editable=False)
    status=models.CharField(choices=STATUS_CHOICES,max_length=30,null=True)
    orderDate=models.DateTimeField(auto_now=True)
    lableSent=models.DateField(null=True,blank=True)
    shippingLableReceived=models.DateField(null=True,blank=True)
    deviceReceived=models.DateField(null=True,blank=True)
    deviceReview=models.CharField(choices=DEVICE_REVIEW_CHOICES,max_length=30,null=True,default=None,blank=True)
    deviceAccepted=models.CharField(choices=ACCEPTANCE_CHOICES,max_length=30,null=True,default=None,blank=True)
    deviceAcceptanceComment=models.CharField(max_length=300,blank=True,null=True)
    paymentMethod=models.CharField(choices=PAYMENT_CHOICES,max_length=30,null=True,blank=True)
    payment_name=models.CharField(max_length=30,blank=True,null=True)
    paymentUsername=models.CharField(max_length=30,blank=True,null=True)
    paymentPhone=models.CharField(max_length=30,blank=True,null=True)
    paymentEmail=models.CharField(max_length=30,blank=True,null=True)
    paymentReferenceNo=models.CharField(max_length=30,blank=True,null=True)
    totalPayment=models.CharField(max_length=30,blank=True,null=True)
    deviceShippingMethod=models.CharField(choices=SHIPPING_CHOICES,max_length=30,null=True)
    deviceTrackingInbound=models.CharField(max_length=30,blank=True,null=True)
    deviceTrackingOutbound=models.CharField(max_length=30,blank=True,null=True)
    #deviceImages=models.ImageField(upload_to='Deviceimages',blank=True,null=True)

    def __str__(self):
        return str(self.orderNo)+ " " +str(self.firstName)+ " " +str(self.lastName)


class GuestUserDevicesInfo(models.Model):
    trade=models.ForeignKey(GuestUserTradeInfo,related_name='devices',on_delete=models.CASCADE)
    deviceNo=models.CharField(max_length=30,blank=True,null=True)
    deviceType=models.CharField(max_length=30,blank=True,null=True)
    deviceModel=models.CharField(max_length=30,blank=True,null=True)
    deviceSerial=models.CharField(max_length=30,blank=True,null=True)
    deviceImei=models.CharField(max_length=30,blank=True,null=True)
    deviceImei2=models.CharField(max_length=30,blank=True,null=True)
    deviceMacAddress=models.CharField(max_length=30,blank=True,null=True)
    deviceCapacity=models.CharField(max_length=30,blank=True,null=True)
    deviceCarrier=models.CharField(max_length=30,blank=True,null=True)
    deviceCondition=models.CharField(max_length=30,blank=True,null=True)
    deviceYear=models.CharField(max_length=30,blank=True,null=True)
    deviceProcessor=models.CharField(max_length=30,blank=True,null=True)
    deviceOffer=models.CharField(max_length=30,blank=True,null=True)
    deviceGeneration=models.CharField(max_length=30,blank=True,null=True)
    deviceSize=models.CharField(max_length=30,blank=True,null=True)
    deviceEdition=models.CharField(max_length=30,blank=True,null=True)
    deviceBand=models.CharField(max_length=30,blank=True,null=True)
    deviceEngraving=models.CharField(max_length=30,blank=True,null=True)
    deviceImages=models.ImageField(upload_to='Deviceimg',blank=True,null=True)
    