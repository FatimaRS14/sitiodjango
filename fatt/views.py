from django.shortcuts import render
from .models import *
# En esta parte se crearan las vistas de la app
def feed(request):
    posts = Post.objects.all()

    context = { 'posts': posts}
    return render(request, 'social\feed.html')

def profile(request):
    return render(request, 'social\profile.html')


