from django.contrib import admin
from .models import Music

# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'rating'
    )


admin.site.register(Music, MusicAdmin)
