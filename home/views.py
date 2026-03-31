from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePost, EditPost
# Create your views here.
def homepage(request):
    posts = Post.objects.all()


    context = {
        "posts" :posts
    }
    return render(request, 'home/homepage.html', context)
def getpost (request,id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request,'home/postdetail.html',context )
def createpost(request):
    # get method to add new form
    form = CreatePost()
    if request.method == "POST":
       # print('Posted Data')
       # print(request.form)
        form=CreatePost(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context ={
        'form':form,
    }
    return render (request, 'home/createpost.html', context)

def editpost(request,id):
    post = Post.objects.get(id=id) # get post with id
    form = EditPost (instance=post)
    if request.method == "POST":
        form=EditPost(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context ={
        'form':form,
    }
    return render (request, 'home/deletepost.html', context)


def deletepost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect ("home")






# python manage.py shell
# from home.models import Post
# post=post.objects.create(title="hello world",description="hi", cost=52)