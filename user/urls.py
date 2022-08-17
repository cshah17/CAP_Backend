from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('UserInfo/', views.UserInfoList.as_view()),
    path('UserInfo/<pk>/', views.UserInfoDetail.as_view()),
    path('UserAddress/', views.UserAddressList.as_view()),
    path('UserAddress/<pk>/', views.UserAddressDetail.as_view()),
    path('UserDeviceInfo/', views.UserDeviceInfoList.as_view()),
    path('UserDeviceInfo/<pk>/', views.UserDeviceInfoDetail.as_view()),
    path('UserTradeInfo/', views.UserTradeInfoList.as_view()),
    path('UserTradeInfo/<pk>/', views.UserTradeInfoDetail.as_view()),
    path('UserPaymentInfo/', views.UserPaymentInfoList.as_view()),
    path('UserPaymentInfo/<pk>/', views.UserPaymentInfoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
    #path('GuestUserInfo/', views.GuestUserInfoList.as_view()),
    #path('GuestUserInfo/<user_id>/', views.GuestUserInfoDetail.as_view()),
    #path('GuestUserAddress/', views.GuestUserAddressList.as_view()),
    #path('GuestUserAddress/<user_id>/', views.GuestUserAddressDetail.as_view()),
    path('GuestUserDeviceInfo/', views.GuestUserDeviceInfoList.as_view()),
    path('GuestUserDeviceInfo/<pk>/', views.GuestUserDeviceInfoDetail.as_view()),
    path('GuestUserTradeInfo/', views.GuestUserTradeInfoList.as_view()),
    path('GuestUserTradeInfo/<pk>/', views.GuestUserTradeInfoDetail.as_view()),
    #path('GuestUserPaymentInfo/', views.GuestUserPaymentInfoList.as_view()),
    #path('GuestUserPaymentInfo/<pk>/', views.GuestUserPaymentInfoDetail.as_view()),
    #path('UserTrade/', views.UserTradeList.as_view()),
    #path('UserTrade/<user_id>/', views.UserTradeDetail.as_view()),
    #path('UserOrder/', views.UserOrderList.as_view()),
    #path('UserOrder/<pk>/', views.UserOrderDetail.as_view()),'''
    
]