from celery import shared_task
from .models import Service, ServiceStatus
from .utils import check_service
from django.core.mail import send_mail

@shared_task
def check_all_services():
    services = Service.objects.filter(is_active=True)

    for service in services:
        result = check_service(service.url)
        ServiceStatus.objects.create(
            service=service,
            **result
        )
        
        #Alert logic
        if service.last_status is None:
            service.last_status = result["is_up"]
            service.save()
            continue
        
        if service.last_status and not result["is_up"]:
            send_mail(
                subject=f"Service DOWN: {service.name}",
                message=f"{service.url} is not reachable.",
                from_email = "watchtower@system.com",
                recipient_list=[service.user.email],
            )
        service.last_status = result["is_up"]
        service.save()
            