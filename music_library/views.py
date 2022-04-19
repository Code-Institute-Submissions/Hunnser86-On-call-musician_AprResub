from django.shortcuts import render
from .models import Music
from django.contrib.auth.decorators import login_required


@login_required()
def music_library(request):
    """ A view to return the music_library"""

    music = Music.objects.all()

    context = {
        'music': music,
    }

    return render(request, 'music_library/music_library.html', context)
