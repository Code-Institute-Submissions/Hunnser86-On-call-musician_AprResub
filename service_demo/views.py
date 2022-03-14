from django.shortcuts import render

from services.models import Service

def service_demo(request):
    """ A view to show all services"""

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'service_demo/service_demo.html', context)
