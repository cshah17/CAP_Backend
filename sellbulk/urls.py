from django.urls import path,include
from .views import InquererListView, GeneralInqueryListView

urlpatterns=[
    path('inquerer/', InquererListView.as_view()),
    path('generalinquery/', GeneralInqueryListView.as_view())
]