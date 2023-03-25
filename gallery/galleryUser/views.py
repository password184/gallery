from django.shortcuts import render, redirect
from .models import About
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

def about(request):
    

    profiles = About.objects.all()
    context = {'profiles': profiles}
    return render(request, 'user/about.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('gallery')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            messages.success(request, 'You successfully logged in')
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')
        
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request, 'user/login.html')

def logoutUser(request):
  logout(request)
  messages.success(request, 'User was logged out')
  return redirect('gallery')

@login_required(login_url='login')
def userAccount(request):
    about = request.user.about
    gallery = about.gallery_set.all()
    context = {'account': about, 'gallerys': gallery}
    return render(request, 'user/account.html', context)

def editAccount(request):
    about = request.user.about
    form = ProfileForm(instance=about)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('user-account')
    context = {'form': form}
    return render(request, 'user/profile_form.html', context)


    
