from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# function home to handle trafic from homepage of the blog
# logic for handling routes

def home(request):
    # data dictionary database
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'Abo'})
