from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from .permission import IsOwner
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo,UserTradeInfo,UserDevicesInfo,UserAddress,GuestUserDevicesInfo,GuestUserTradeInfo,UserPaymentInfo
#GuestUserPaymentInfo
#GuestUserAddress,GuestUserDevicesInfo,GuestUserInfo,GuestUserTradeInfo
from .serializers import UserInfoSerializer,UserTradeInfoSerializer,UserDeviceInfoSerializer,UserAddressSerializer,GuestUserDeviceInfoSerializer,GuestUserTradeInfoSerializer,UserSerializer,UserPaymentInfoSerializer
#GuestUserInfoSerializer,GuestUserTradeInfoSerializer,GuestUserAddressSerializer,GuestUserDeviceInfoSerializer
#,GuestUserOrderSerializer,UserOrder
from django.contrib.auth.models import User
#from django.contrib.auth.models import Anonymoususer
from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
# Create your views here.


class UserInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    #lookup_field='id'

class UserAddressList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    #lookup_field='user_id'

class UserDeviceInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserDevicesInfo.objects.all()
    serializer_class = UserDeviceInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserDeviceInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserDevicesInfo.objects.all()
    serializer_class = UserDeviceInfoSerializer
    #lookup_field='id'

class UserPaymentInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserPaymentInfo.objects.all()
    serializer_class = UserPaymentInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPaymentInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserPaymentInfo.objects.all()
    serializer_class = UserPaymentInfoSerializer
    #lookup_field='id'

class UserTradeInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserTradeInfo.objects.all()
    serializer_class = UserTradeInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    
    def perform_create(self, serializer):
        created_object=serializer.save(user=self.request.user)
        username=created_object.user
        orderno=created_object.orderNo
        send_mail('Your order has been received with Order #{}'.format(orderno),'hi {},\nCongratulations! your order has been placed successflly'.format(username),'{}'.format(settings.EMAIL_HOST_USER),[created_object.user.email,], fail_silently=False,)

class UserTradeInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserTradeInfo.objects.all()
    serializer_class = UserTradeInfoSerializer
    #lookup_field='id'



'''class UserOrderList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    #lookup_field='user_id'''

#Guest User erializer View
'''class GuestUserInfoList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserInfo.objects.all()
    serializer_class = GuestUserInfoSerializer
    #filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save()

class GuestUserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserInfo.objects.all()
    serializer_class = GuestUserInfoSerializer
    #lookup_field='user_id

class GuestUserPaymentInfoList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsOwner]
    queryset = GuestUserPaymentInfo.objects.all()
    serializer_class = GuestUserPaymentInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GuestUserPaymentInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsOwner]
    queryset = GuestUserPaymentInfo.objects.all()
    serializer_class = GuestUserPaymentInfoSerializer
    #lookup_field='id'''

class GuestUserTradeInfoList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserTradeInfo.objects.all()
    serializer_class = GuestUserTradeInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    
    def perform_create(self, serializer):
        created_object=serializer.save()
        username=created_object.firstName
        orderno=created_object.orderNo
        send_mail('Your order has been received with Order #{}'.format(orderno),'hi {},\nCongratulations! your order has been placed successflly'.format(username),'{}'.format(settings.EMAIL_HOST_USER),[created_object.email,], fail_silently=False,)



class GuestUserTradeInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserTradeInfo.objects.all()
    serializer_class = GuestUserTradeInfoSerializer
    #lookup_field='id'


'''class GuestUserAddressList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserAddress.objects.all()
    serializer_class = GuestUserAddressSerializer
    #filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save()

class GuestUserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserAddress.objects.all()
    serializer_class = GuestUserAddressSerializer
    lookup_field='user_id'''

class GuestUserDeviceInfoList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserDevicesInfo.objects.all()
    serializer_class = GuestUserDeviceInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save()

class GuestUserDeviceInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserDevicesInfo.objects.all()
    serializer_class = GuestUserDeviceInfoSerializer
    #lookup_field='id'

'''class GuestUserOrderList(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserOrder.objects.all()
    serializer_class = GuestUserOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    
    def perform_create(self, serializer):
        serializer.save(user=None)

class GuestUserOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = GuestUserOrder.objects.all()
    serializer_class = GuestUserOrderSerializer
    #lookup_field='user_id'''

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer