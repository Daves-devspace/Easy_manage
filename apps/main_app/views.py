
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm




@login_required
def home(request):
    return render(request, 'home/index.html')


def login_user(request):
    if request.method == 'GET':
       form = LoginForm()
       return render(request,"home/login_form.html",{"form":form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
        messages.error(request,"Invalid username or password")    
        return render(request,"home/login_form.html",{"form":form})
    
@login_required    
def logout_user(request):
    logout(request)
    return redirect('login')





