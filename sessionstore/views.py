from django.shortcuts import render
from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework import permissions
from .serializers import SessionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
# Create your views here.

class SessionList(generics.ListCreateAPIView):
    #permission_classes = [Allowany]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    #lookup_field='session_key'
