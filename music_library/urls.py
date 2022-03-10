from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_library, name='music_library')
]
