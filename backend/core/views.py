# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

# ------------------------------------------------------------
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Service, ServiceStatus
from .utils import check_service

class CheckServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk, user=request.user)
        result = check_service(service.url)

        ServiceStatus.objects.create(
            service=service,
            **result
        )
        return Response(result)

        # return Response({
        #     "service": service.name,
        #     "is_up": service_status.is_up,
        #     "status_code": service_status.status_code,
        #     "response_time": service_status.response_time,
        #     "checked_at": service_status.checked_at
        # })