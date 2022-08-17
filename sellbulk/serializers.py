from rest_framework import serializers
from .models import Devices,Inquerer,GeneralInquery


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ['deviceType','deviceCondition','deviceQuantity']

class InquererSerializer(serializers.ModelSerializer):
    devices= DevicesSerializer(many=True,)

    class Meta:
        model = Inquerer
        fields = ['inqueryNo','devices','email', 'firstName', 'lastName']

    def create(self, validated_data):
        devices_data = validated_data.pop('devices')
        inquerer = Inquerer.objects.create(**validated_data)
        for device_data in devices_data:
            Devices.objects.create(inquerer=inquerer, **device_data)
        return inquerer


class GeneralInquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInquery
        fields = ['caseNo','description','subject','firstName','lastName','topic','email','phoneNumber']
