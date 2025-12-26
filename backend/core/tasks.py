from celery import shared_task
from .models import Service, ServiceStatus
from .utils import check_service

@shared_task
def check_all_services():
    services = Service.objects.filter(is_active=True)

    for service in services:
        result = check_service(service.url)
        ServiceStatus.objects.create(
            service=service,
            **result
        )