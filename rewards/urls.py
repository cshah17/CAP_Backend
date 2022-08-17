from django.urls import path,include
from .views import RewardsList,UserRewardsList

urlpatterns=[
    path('UserRewards/', UserRewardsList.as_view()),
    #path('UserRewards/<pk>', UserDetailView.as_view())
    #path('Rewards/<pk>', UserRewardsDetailView.as_view())
    path('Rewards/', RewardsList.as_view())
]