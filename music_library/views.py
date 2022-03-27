from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def music_library(request):
    """ A view to return the music_library"""

    return render(request, 'music_library/music_library.html')
