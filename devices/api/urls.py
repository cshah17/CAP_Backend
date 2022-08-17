from django.urls import path
from .views import IphoneListView, IphoneDetailView, MacbookListView, MacbookDetailView,IpadListView,IpadDetailView,SamsungPhoneListView,SamsungPhoneDetailView,GooglePhoneListView,GooglePhoneDetailView,IpodListView,IpodDetailView,AirpodsDetailView,AirpodsListView
from .views import IwatchListView, IwatchDetailView, DevicesListView, DevicesDetailView, IphoneCreateView
urlpatterns =[
    path('iphoneapi',IphoneListView.as_view()),
     path('iphoneapi/create',IphoneCreateView.as_view()),
    path('iphoneapi/<pk>/',IphoneDetailView.as_view()),
    path('macbookapi/',MacbookListView.as_view()),
    path('macbookapi/<pk>/',MacbookDetailView.as_view()),
    path('ipadapi',IpadListView.as_view()),
    path('ipadapi/<pk>/',IpadDetailView.as_view()),
    path('samsungapi/',SamsungPhoneListView.as_view()),
    path('samsungapi/<pk>/',SamsungPhoneDetailView.as_view()),
    path('googleapi/',GooglePhoneListView.as_view()),
    path('googleapi/<pk>/',GooglePhoneDetailView.as_view()),
    path('ipodapi/',IpodListView.as_view()),
    path('ipodapi/<pk>/',IpodDetailView.as_view()),
    path('iwatchapi/',IwatchListView.as_view()),
    path('iwatchapi/<pk>/',IwatchDetailView.as_view()),
    path('devicesapi/',DevicesListView.as_view()),
    path('devicesapi/<pk>',DevicesDetailView.as_view()),
    path('airpodsapi/',AirpodsListView.as_view()),
    path('airpodsapi/<pk>',AirpodsDetailView.as_view()),
    
    
]