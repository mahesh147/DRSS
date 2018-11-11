from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

from relief_center.models import ReliefCenter


def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})

    else:
        return render(request, 'accounts/signup.html')


def login(request):

    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


@login_required(login_url="/accounts/signup")
def dashboard(request):
    relief_centers = ReliefCenter.objects.all().filter(admin=request.user)
    print('Relief center = ' + str(relief_centers))
    return render(request, 'accounts/dashboard.html', {'relief_centers': relief_centers})
