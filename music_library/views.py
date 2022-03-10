from django.shortcuts import render


def music_library(request):
    """ A view to return the music_library"""

    return render(request, 'music_library/music_library.html')
