"""
A model to display music in the music library.
"""
from django.db import models


class Music(models.Model):

    """
    A meta class to change the verbose name/plural name
    """
    class Meta:
        verbose_name_plural = 'Music'

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=400)
    url = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
