from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('session/', views.SessionList.as_view()),
    path('session/<pk>', views.SessionDetail.as_view()),
]