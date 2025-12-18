from rest_framework import serializers
from . models import Service

class ServiceSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "url", "is_active", "created_at"]