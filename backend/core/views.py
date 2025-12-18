# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

class HealthCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"status": "ok"})
# ------------------------------------------------------------
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Service
from .serializers import ServiceSeriallizer

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSeriallizer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Service.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)