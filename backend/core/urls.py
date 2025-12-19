from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, HealthCheckView, CheckServiceView

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")

urlpatterns = router.urls + [
    path("health/", HealthCheckView.as_view()),
    path("services/<int:pk>/check/", CheckServiceView.as_view()),
    ]
