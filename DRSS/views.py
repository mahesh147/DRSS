from django.shortcuts import render


def home(request):
    return render(request, 'drss/home.html')
