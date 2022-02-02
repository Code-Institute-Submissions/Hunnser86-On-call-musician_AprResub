"""
Import admin and Service
"""
from django.contrib import admin
from .models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    """
    A class to display certain information to the Backend.
   """
    list_display = (
        'name',
        'description',
        'price',
        'frequency',
        'access',
        'original_music',
        'rating',
        'image',
    )

    ordering = ('price',)


admin.site.register(Service, ServiceAdmin)
