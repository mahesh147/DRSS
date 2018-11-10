from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import ReliefCenter


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['location'] and request.POST['contact'] and request.POST['disaster']:
            relief_center = ReliefCenter()
            print('Contact: ' + request.POST['disaster'])
            relief_center.location = request.POST['location']
            relief_center.contact = request.POST['contact']
            relief_center.type_of_disaster = request.POST['disaster']
            relief_center.donation_received = 0
            relief_center.save()
            return redirect('dashboard')
        else:
            return render(request, 'relief_center/create.html', {'error': 'All fields are required'})

    else:
        return render(request, 'relief_center/create.html')

    return render(request, 'relief_center/create.html')
