from django.shortcuts import render

# Create your views here.
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

def create_user(request):
    form=UserCreationForm()
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'users/success.html')
    context={
    'form': form
    }
    return render(request, 'users/create_user.html',context)



def login_user(request):
    form= UserLoginForm()
    if request.method == 'POST':
        form= UserLoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user= authenticate (request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return render(request, 'users/success.html')
                return HttpResponse("Login successfull")
            else:
                form.add_error( None, 'Invaldid usrername or password')
    context ={
        'form':form 
    }
    return render(request, 'users/login.html', context)

def Logout_user(request):
    logout(request)
    return HttpResponse('logout successful')


