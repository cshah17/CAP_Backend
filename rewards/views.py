from django.shortcuts import render

# Create your views here.
from .serializers import RewardsSerializer,UserRewardsSerializer
from .models import Rewards,UserRewards
from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend



class RewardsList(generics.ListCreateAPIView):
    permissions_class = [permissions.AllowAny]
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save()



class UserRewardsList(generics.ListCreateAPIView):
    permissions_class = [permissions.IsAuthenticated]
    queryset = UserRewards.objects.all()
    serializer_class = UserRewardsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
