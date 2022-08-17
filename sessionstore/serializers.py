from django.contrib.sessions.models import Session
from rest_framework import serializers

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Session
        fields=['session_key','session_data','expire_date']





