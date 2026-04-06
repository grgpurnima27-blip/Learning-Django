from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePost, EditPost
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    posts = Post.objects.all()


    context = {
        "posts" :posts
    }
    return render(request, 'home/homepage.html', context)

@login_required(login_url="login")
def getpost (request,id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request,'home/postdetail.html',context )
@login_required(login_url="login")
def createpost(request):
    # get method to add new form
    form = CreatePost()
    if request.method == "POST":
        user= request.user
       # print('Posted Data')
       # print(request.form)
        form=CreatePost(data=request.POST, files=request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user= request.user
            post.save()
            return redirect("home")
    context ={
        'form':form,
    }
    return render (request, 'home/createpost.html', context)

@login_required(login_url="login")

def editpost(request,id):
    post = Post.objects.get(id=id) # get post with id
    form = EditPost (instance=post)
    if request.method == "POST":
        if post.user != request.user:
            return HttpResponse ("You are not allowed to edit this post")
        form=EditPost(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context ={
        'form':form,
    }
    return render (request, 'home/deletepost.html', context)

@login_required(login_url="login")
def deletepost(request,id):
    post=Post.objects.get(id=id)
    if post.user != request.user:
        return HttpResponse ("You are not allowed to edit this post")
    post.delete()
    return redirect ("home")






# python manage.py shell
# from home.models import Post
# post=post.objects.create(title="hello world",description="hi", cost=52)