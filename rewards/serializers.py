from rest_framework import serializers
from .models import *


class UserRewardsSerializer(serializers.ModelSerializer):
    user=serializers.CharField(max_length=20, min_length=None, allow_blank=True, trim_whitespace=True)
    
    class Meta:
        model = UserRewards
        fields = ['promocode','user']

class RewardsSerializer(serializers.ModelSerializer):
    code=models.CharField(max_length=30,null=True)
    discount=models.CharField(max_length=30,null=True,blank=True)
    bonus=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=130,null=True,blank=True)
    condition=models.CharField(max_length=120,null=True,blank=True)
    
    class Meta:
       
        model = Rewards
        fields = ['id','description','code','bonus','condition','discount']

    '''def create(self, validated_data):
        codes_data = validated_data.pop('code')
        user = User.objects.create(**validated_data)
        for code_data in codes_data:
            UserRewards.objects.create(user=user, **code_data)
        return user

    def update(self, instance, validated_data):
        codes_data = validated_data.pop('code')
        code= (instance.user).all()
        codes= list(code)
        instance.save()

        for code_data in codes_data:
            #orders_data = validated_data.pop('usertrade')
            code = codes.pop(0)
            code.deviceNo = devices_data.get('deviceNo', device.deviceNo)
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
