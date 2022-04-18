from django.db import models

class Music(models.Model):

    """
    A class to display the songs for the music library

    """
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=400)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)

    def __str__(self):
        return self.name
