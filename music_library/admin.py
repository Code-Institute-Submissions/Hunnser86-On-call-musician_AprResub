from django.contrib import admin
from .models import Music

# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'iframe',
        'description',
        'rating'
    )


admin.site.register(Music, MusicAdmin)
