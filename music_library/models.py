from django.db import models

class Music(models.Model):

    """
    A class to display the songs for the music library

    """
    class Meta:
        verbose_name_plural = 'Music'

    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=400)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)

    def __str__(self):
        return self.name
