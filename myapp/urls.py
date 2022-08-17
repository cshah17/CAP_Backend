"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets, urls
from django.views.generic import TemplateView, RedirectView
from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('devices.urls')),
    path('', include('user.urls')),
    path('', include('rewards.urls')),
    path('', include('sessionstore.urls')),
    path('api/', include('sellbulk.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('devices.api.urls')),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", confirm_email,name='account_confirm_email'),
    path('accounts/', include('allauth.urls')),
]
