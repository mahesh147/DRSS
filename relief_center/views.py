from django.shortcuts import render


def create(request):
    return render(request, 'relief_center/create.html')
