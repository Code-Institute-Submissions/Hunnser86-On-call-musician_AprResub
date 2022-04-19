from django.contrib import admin
from .models import Music

# Register your models here.
"""
A class to tell the admin which fields to display
"""
class MusicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'url',
        'image',
    )


admin.site.register(Music, MusicAdmin)
