from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import ReliefCenter
from wanted_item.models import WantedItem


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['location'] and request.POST['contact'] and request.POST['disaster']:
            relief_center = ReliefCenter()
            relief_center.location = request.POST['location']
            relief_center.contact = request.POST['contact']
            relief_center.type_of_disaster = request.POST['disaster']
            relief_center.donation_received = 0
            relief_center.admin = request.user
            relief_center.save()
            return redirect('dashboard')
        else:
            return render(request, 'relief_center/create.html', {'error': 'All fields are required'})

    else:
        return render(request, 'relief_center/create.html')

    return render(request, 'relief_center/create.html')


@login_required(login_url="/accounts/signup")
def view(request, relief_center_id):
    relief_center = get_object_or_404(ReliefCenter, pk=relief_center_id)
    wanted_items = WantedItem.objects.all().filter(relief_center_id=relief_center.id)
    print(wanted_items)
    if request.user == relief_center.admin:
        return render(request, 'relief_center/view.html', {'relief_center': relief_center, 'wanted_items': wanted_items})
    else:
        return redirect('dashboard')


@login_required(login_url="/accounts/signup")
def update(request, relief_center_id):
    relief_center = get_object_or_404(ReliefCenter, pk=relief_center_id)
    if request.user == relief_center.admin:
        if request.method == 'POST':
            if request.POST['location'] and request.POST['contact'] and request.POST['disaster']:
                relief_center.location = request.POST['location']
                relief_center.contact = request.POST['contact']
                relief_center.type_of_disaster = request.POST['disaster']
                relief_center.donation_received = request.POST['donation']
                relief_center.admin = request.user
                relief_center.save()
                return redirect('dashboard')
            else:
                return render(request, 'relief_center/update.html', {'error': 'All fields are required', 'relief_center': relief_center})
        else:
            return render(request, 'relief_center/update.html', {'relief_center': relief_center})
    else:
        return redirect('dashboard')


@login_required(login_url="/accounts/signup")
def delete(request, relief_center_id):
    relief_center = get_object_or_404(ReliefCenter, pk=relief_center_id)
    if request.user == relief_center.admin:
        if request.method == 'POST':
            relief_center.delete()
            return redirect('dashboard')

        else:
            return render(request, 'relief_center/delete.html', {'relief_center': relief_center})
    else:
        return redirect('dashboard')
