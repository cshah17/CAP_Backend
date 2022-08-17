from .models import UserInfo,UserTradeInfo,UserAddress,UserDevicesInfo,GuestUserDevicesInfo,GuestUserTradeInfo,UserPaymentInfo
#UserOrder,GuestUserPaymentInfo,
from rest_framework import serializers
from django.contrib.auth.models import User



class UserAddressSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model= UserAddress
        fields=['id','user','firstName','lastName','addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress']

class UserInfoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    secondary_email=serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    phoneNumber=serializers.CharField(max_length=20, min_length=None, allow_blank=True, trim_whitespace=True)
    class Meta:
        model = UserInfo
        fields = ['id','user_id','user','secondary_email','phoneNumber']

    '''def create(self, validated_data):
        addresses_data = validated_data.pop('useraddress')
        userinfo = UserInfo.objects.create(**validated_data)
        for address_data in addresses_data:
            UserAddress.objects.create(userinfo=userinfo, **address_data)
        return userinfo

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('useraddress')
        address = (instance.useraddress).all()
        address = list(address)
        instance.secondary_email = validated_data.get('secondary_email', instance.secondary_email)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.save()
        for addresses_data in addresses_data:
            address = address.pop(0)
            address.addressType = addresses_data.get('addressType', address.addressType)
            address.addressLine1 = addresses_data.get('addressLine1', address.addressLine1)
            address.addressLine2 = addresses_data.get('addressLine2', address.addressLine2)
            address.city = addresses_data.get('city', address.city)
            address.state = addresses_data.get('state', address.state)
            address.zipcode = addresses_data.get('zipcode', address.zipcode)
            address.primaryAddress = addresses_data.get('primaryAddress', address.primaryAddress)
            address.save()
        return instance'''

class UserDeviceInfoSerializer(serializers.ModelSerializer):
    trade=serializers.ReadOnlyField(source='trade.orderNo')
    class Meta:
        model=UserDevicesInfo
        fields=['id','trade','deviceType','deviceModel','deviceSerial','deviceImei','deviceImei2','deviceMacAddress','deviceCapacity','deviceCarrier','deviceCondition','deviceYear','deviceProcessor','deviceOffer','deviceGeneration','deviceSize','deviceEdition','deviceBand','deviceEngraving']

class UserPaymentInfoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=UserPaymentInfo
        fields=['user','id','paymentMethod','name','username','Phone','email']

class UserTradeInfoSerializer(serializers.ModelSerializer):
    
    address=UserAddressSerializer
    email=serializers.ReadOnlyField(source='user.email')
    user=serializers.ReadOnlyField(source='user.username')
    devices=UserDeviceInfoSerializer(many=True)
    paymentMethod=UserPaymentInfoSerializer
    class Meta:
        model = UserTradeInfo
        fields = ['id','user','email','devices','address','paymentMethod','orderNo','status','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceShippingMethod','deviceTrackingInbound','deviceTrackingOutbound','totalPayment']
    
    def create(self, validated_data):
        devices_data = validated_data.pop('devices')
        trade = UserTradeInfo.objects.create(**validated_data)
        for  device_data in  devices_data:
            UserDevicesInfo.objects.create(trade=trade, **device_data)
        return trade


    def update(self, instance, validated_data):
        devices_data = validated_data.pop('devices')
        device= (instance.trade).all()
        devices = list(device)
        instance.save()

        for device_data in devices_data:
            #orders_data = validated_data.pop('usertrade')
            device = devices.pop(0)
            device.deviceType = devices_data.get('deviceType', device.deviceType)
            device.deviceModel = devices_data.get('deviceModel', device.deviceModel)
            device.deviceCapacity = devices_data.get('deviceCapacity', device.deviceCapacity)
            device.deviceCarrier = devices_data.get('deviceCarrier', device.deviceCarrier)
            device.deviceCondition = devices_data.get('deviceCondition', device.deviceCondition)
            device.deviceYear = devices_data.get('deviceYear', device.deviceYear)
            device.deviceProcessor = devices_data.get('deviceProcessor', device.deviceProcessor)
            device.deviceOffer = devices_data.get('deviceOffer', device.deviceOffer)
            device.deviceGeneration = devices_data.get('deviceGeneration', device.deviceGeneration)
            device.deviceSize = devices_data.get('deviceSize', device.deviceSize)
            device.deviceEdition = devices_data.get('deviceEdition', device.deviceEdition)
            device.deviceBand = devices_data.get('deviceBand', device.deviceBand)
            device.deviceEngraving = devices_data.get('deviceEngraving', device.deviceEngraving)
            device.save()
        return instance

    '''class UserTradeSerializer(serializers.ModelSerializer):
    
    #user=serializers.ReadOnlyField(source='address.userinfo.user.username')
    address=serializers.ReadOnlyField(source='address.addressLine1')
    #user_id=serializers.ReadOnlyField(source='userorder.user.id')
    

    class Meta:
        model = UserTradeInfo
        fields = ['tradeReferenceNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','paymentMethod','deviceShippingMethod','deviceTrackingInbound','deviceTrackingOutbound','totalPayment']  
        
    class UserOrderSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    usertrade=UserTradeInfoSerializer(many=True)
   

    class Meta:
        model = UserOrder
        fields = ['id','user','usertrade']
    


     def create(self, validated_data):
        orders_data = validated_data.pop('usertrade')
        userorder= UserOrder.objects.create(**validated_data)
        for order_data in orders_data:
            UserTradeInfo.objects.create(userorder=userorder, **order_data)
        return userorder'''

    '''def update(self, instance, validated_data):
        orders_data = validated_data.pop('usertrade')
        orders = (instance.usertrade).all()
        order = list(orders)
        instance.save()

        for order_data in orders_data:
            devices_data = validated_data.pop('usertradeinfo')
            devices = (instance.usertrade).get().usertradeinfo.all()
            devices = list(devices)
            for device_data in devices_data:
                device = devices.pop(0)
                device.deviceType = device_data.get('deviceType', device.deviceType)
                device.deviceModel = device_data.get('deviceModel', device.deviceModel)
                device.deviceCapacity = device_data.get('deviceCapacity', device.deviceCapacity)
                device.deviceCarrier = device_data.get('deviceCarrier', device.deviceCarrier)
                device.deviceCondition = device_data.get('deviceCondition', device.deviceCondition)
                device.deviceYear = device_data.get('deviceYear', device.deviceYear)
                device.deviceProcessor = device_data.get('deviceProcessor', device.deviceProcessor)
                device.deviceOffer = device_data.get('deviceOffer', device.deviceOffer)
                device.deviceGeneration = device_data.get('deviceGeneration', device.deviceGeneration)
                device.deviceSize = devices_data.get('deviceSize', device.deviceSize)
                device.deviceEdition = device_data.get('deviceEdition', device.deviceEdition)
                device.deviceBand = device_data.get('deviceBand', device.deviceBand)
                device.deviceEngraving = device_data.get('deviceEngraving', device.deviceEngraving)
                device.save()
            order=orders.pop(0)
            order.tradeReferenceNo = order_data.get('tradeReferenceNo', order.tradeReferenceNo)
            order.status = order_data.get('status', order.status)
            order.orderDate = order_data.get('orderDate', order.orderDate)
            order.lableSent = order_data.get('lableSent', order.lableSent)
            order.shippingLableReceived = order_data.get('shippingLableReceived', order.shippingLableReceived)
            order.deviceReceived = order_data.get('deviceReceived', order.deviceReceived)
            order.deviceReview = order_data.get('deviceReview', order.deviceReview)
            order.deviceAccepted = order_data.get('deviceAccepted', order.deviceAccepted)
            order.deviceAcceptanceComment = order_data.get('deviceAcceptanceComment', order.deviceAcceptanceComment)
            oreder.totalPayment=order_data.get('paymentMethod',order.paymentMethod)
            order.paymentReferenceNo = order_data.get('paymentReferenceNo', order.paymentReferenceNo)
            order.deviceShippingMethod = order_data.get('deviceShippingMethod', order.deviceShippingMethod)
            order.deviceTrackingInbound = order_data.get('deviceTrackingInbound', order.deviceTrackingInbound)
            order.deviceTrackingOutbound = order_data.get('deviceTrackingOutbound', order.deviceTrackingOutbound)
            order.save()
        return instance
        




class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        Model=UserDevicesInfo
        

class UserDeviceInfoSerializer(serializers.ModelSerializer):
    trade=serializers.ReadOnlyField(source='usertradeinfo.orderNo')
    class Meta:
        model=UserDevicesInfo
        fields=['trade','deviceNo','deviceType','deviceModel','deviceCapacity','deviceCarrier','deviceCondition','deviceYear','deviceProcessor','deviceOffer','deviceGeneration','deviceSize','deviceEdition','deviceBand','deviceEngraving']

class UserTradeInfoSerializer(serializers.ModelSerializer):
    
    #address=serializers.ReadOnlyField(source='address.addressLine1')
    user=serializers.ReadOnlyField(source='user.username')
    devices=UserDeviceInfoSerializer(many=True)

    class Meta:
        model = UserTradeInfo
        fields = ['user','devices','orderNo','status','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceShippingMethod','deviceTrackingInbound','deviceTrackingOutbound','totalPayment']
    
    def create(self, validated_data):
        devices_data = validated_data.pop('devices')
        trade = UserTradeInfo.objects.create(**validated_data)
        for  device_data in  devices_data:
            UserDevicesInfo.objects.create(trade=trade, **device_data)
        return trade


    def update(self, instance, validated_data):
        devices_data = validated_data.pop('devices')
        device= (instance.trade).all()
        devices = list(device)
        instance.save()

        for device_data in devices_data:
            #orders_data = validated_data.pop('usertrade')
            device = devices.pop(0)
            device.deviceNo = devices_data.get('deviceNo', device.deviceNo)
            device.deviceType = devices_data.get('deviceType', device.deviceType)
            device.deviceModel = devices_data.get('deviceModel', device.deviceModel)
            device.deviceCapacity = devices_data.get('deviceCapacity', device.deviceCapacity)
            device.deviceCarrier = devices_data.get('deviceCarrier', device.deviceCarrier)
            device.deviceCondition = devices_data.get('deviceCondition', device.deviceCondition)
            device.deviceYear = devices_data.get('deviceYear', device.deviceYear)
            device.deviceProcessor = devices_data.get('deviceProcessor', device.deviceProcessor)
            device.deviceOffer = devices_data.get('deviceOffer', device.deviceOffer)
            device.deviceGeneration = devices_data.get('deviceGeneration', device.deviceGeneration)
            device.deviceSize = devices_data.get('deviceSize', device.deviceSize)
            device.deviceEdition = devices_data.get('deviceEdition', device.deviceEdition)
            device.deviceBand = devices_data.get('deviceBand', device.deviceBand)
            device.deviceEngraving = devices_data.get('deviceEngraving', device.deviceEngraving)
            device.save()
        return instance'''

#Guest Serializer

'''class GuestUserAddressSerializer(serializers.ModelSerializer):
    #guestuser=serializers.ReadOnlyField(source='guestUserInfo.email')
    class Meta:
        model= GuestUserAddress
        fields=['addressType','addressLine1','addressLine2','city','state','zipcode',]

class GuestUserInfoSerializer(serializers.ModelSerializer):
    firstName=serializers.CharField(max_length=30, min_length=None, allow_blank=True, trim_whitespace=True)
    lastName=serializers.CharField(max_length=30, min_length=None, allow_blank=True, trim_whitespace=True)
    email=serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    phoneNumber=serializers.CharField(max_length=20, min_length=None, allow_blank=True, trim_whitespace=True)
    class Meta:
        model = GuestUserInfo
        fields = ['firstName','lastName','email','phoneNumber']'''


class GuestUserDeviceInfoSerializer(serializers.ModelSerializer):
    trade=serializers.ReadOnlyField(source='trade.orderNo')
    class Meta:
        model=GuestUserDevicesInfo
        fields=['id','trade','deviceNo','deviceType','deviceModel','deviceSerial','deviceImei','deviceImei2','deviceMacAddress','deviceCapacity','deviceCarrier','deviceCondition','deviceYear','deviceProcessor','deviceOffer','deviceGeneration','deviceSize','deviceEdition','deviceBand','deviceEngraving']



class GuestUserTradeInfoSerializer(serializers.ModelSerializer):
    devices=GuestUserDeviceInfoSerializer(many=True)
    firstName=serializers.CharField(max_length=30, min_length=None, allow_blank=True, trim_whitespace=True)
    lastName=serializers.CharField(max_length=30, min_length=None, allow_blank=True, trim_whitespace=True)
    email=serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    phoneNumber=serializers.CharField(max_length=20, min_length=None, allow_blank=True, trim_whitespace=True)
   


    class Meta:
        model = GuestUserTradeInfo
        fields = ['id','firstName','lastName','email','devices','paymentMethod','payment_name','paymentUsername','paymentPhone','paymentEmail','phoneNumber','addressType','addressLine1','addressLine2','city','state','zipcode','orderNo','status','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','deviceShippingMethod','deviceTrackingInbound','deviceTrackingOutbound','totalPayment']
    
    def create(self, validated_data):
        devices_data = validated_data.pop('devices')
        trade = GuestUserTradeInfo.objects.create(**validated_data)
        for  device_data in  devices_data:
            GuestUserDevicesInfo.objects.create(trade=trade, **device_data)
        return trade


    def update(self, instance, validated_data):
        devices_data = validated_data.pop('devices')
        device= (instance.trade).all()
        devices = list(device)
        instance.save()

        for device_data in devices_data:
            #orders_data = validated_data.pop('usertrade')
            device = devices.pop(0)
            device.deviceNo = devices_data.get('deviceNo', device.deviceNo)
            device.deviceType = devices_data.get('deviceType', device.deviceType)
            device.deviceModel = devices_data.get('deviceModel', device.deviceModel)
            device.deviceCapacity = devices_data.get('deviceCapacity', device.deviceCapacity)
            device.deviceCarrier = devices_data.get('deviceCarrier', device.deviceCarrier)
            device.deviceCondition = devices_data.get('deviceCondition', device.deviceCondition)
            device.deviceYear = devices_data.get('deviceYear', device.deviceYear)
            device.deviceProcessor = devices_data.get('deviceProcessor', device.deviceProcessor)
            device.deviceOffer = devices_data.get('deviceOffer', device.deviceOffer)
            device.deviceGeneration = devices_data.get('deviceGeneration', device.deviceGeneration)
            device.deviceSize = devices_data.get('deviceSize', device.deviceSize)
            device.deviceEdition = devices_data.get('deviceEdition', device.deviceEdition)
            device.deviceBand = devices_data.get('deviceBand', device.deviceBand)
            device.deviceEngraving = devices_data.get('deviceEngraving', device.deviceEngraving)
            device.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']