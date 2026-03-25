from django.shortcuts import render
from .models import Post
# Create your views here.
def homepage(request):
    posts = Post.objects.all()


    context = {
        "posts" :posts
    }
    return render(request, 'home/homepage.html', context)
def about(request):
    return render (request,'home/about.html')