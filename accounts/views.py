"""from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import  SignInForm, SignUpForm
from django.contrib.auth.models import User 

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'You already have an account. Please sign in.')
                return redirect('signup')  # Redirect to signin page with error message
            else:        
                user = form.save()
                login(request, user)  # Log in the user after account creation
                messages.success(request, 'Congratulations! You have completed your account setup.')
                return redirect('home')  # Redirect to home with success message 
        else:
            print(form.errors)             
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, 'Invalid username or password. Please try again.')             
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')  # Redirect to your home page after logout"""

from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignInForm, SignUpForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken. Please choose a different one.')
                return redirect('signup')  # Redirect back to signup with error message

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email address is already registered.')
                return redirect('signup')  # Redirect back to signup with error message

            user = form.save()
            login(request, user)  # Log in the user after account creation
            messages.success(request, 'Congratulations! You have completed your account setup.')
            return redirect('home')  # Redirect to home with success message 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')  # Redirect to your home page after logout

@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)