"""
Import render and Service model
"""
from django.shortcuts import render
from .models import Service


def all_services(request):
    """ A view to show all products"""

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)
