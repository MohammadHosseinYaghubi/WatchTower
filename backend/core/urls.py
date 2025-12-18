from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, HealthCheckView

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")

urlpatterns = router.urls + [
    path("health/", HealthCheckView.as_view()),
    ]
