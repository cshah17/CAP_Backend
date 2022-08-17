from django.shortcuts import render

# Create your views here.
from .serializers import DevicesSerializer,InquererSerializer, GeneralInquerySerializer
from .models import Inquerer,Devices, GeneralInquery
from rest_framework import generics
from rest_framework import permissions
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings



class InquererListView(generics.ListCreateAPIView):
    permissions_class = [permissions.AllowAny]
    queryset = Inquerer.objects.all()
    serializer_class = InquererSerializer
    #send_email_confirmation(modified=instance)

    def perform_create(self, serializer):
        created_object=serializer.save()
        username=created_object.firstName
        orderno=created_object.inqueryNo
        send_mail('Your inquery has been received with Case #{}'.format(orderno),'Hi {},\nCongratulations! your Inquery has been received successflly!\n\rPlease allow us 48 hour to address your query and return back to you\n\r'.format(username),'{}'.format(settings.EMAIL_HOST_USER),[created_object.email,], fail_silently=False,)


class GeneralInqueryListView(generics.ListCreateAPIView):
    permissions_class = [permissions.AllowAny]
    queryset = GeneralInquery.objects.all()
    serializer_class = GeneralInquerySerializer
    #send_email_confirmation(modified=instance)
    
    def perform_create(self, serializer):
        created_object=serializer.save()
        username=created_object.firstName
        orderno=created_object.caseNo
        send_mail('Your case has been received with Case #{}'.format(orderno),'Hi {},\nCongratulations! your Case has been received successflly!\n\rPlease allow us 48 hour to address your query and return back to you\n\r'.format(username),'{}'.format(settings.EMAIL_HOST_USER),[created_object.email,], fail_silently=False,)