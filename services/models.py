"""
A model for the services on offer.
"""
from django.db import models


class Service(models.Model):
    """
    A class of service to return the correct information to the frontend.
    """
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subscription = models.CharField(max_length=254, default='Subscription')
    access = models.CharField(max_length=254, default='Access')
    original_music = models.CharField(max_length=254, default='Original Music')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
