from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . models import WantedItem
from . models import ReliefCenter


@login_required(login_url="/accounts/signup")
def create(request, relief_center_id):
    relief_center = get_object_or_404(ReliefCenter, pk=relief_center_id)
    if request.method == 'POST':
        if request.POST['name'] and request.POST['urgency_level'] and request.POST['description'] and request.POST['category'] and request.POST['quantity']:
            wanted_item = WantedItem()
            wanted_item.item_name = request.POST['name']
            wanted_item.urgency_level = request.POST['urgency_level']
            wanted_item.description = request.POST['description']
            wanted_item.category = request.POST['category']
            wanted_item.quantity = request.POST['quantity']
            wanted_item.relief_center_id = relief_center.id
            wanted_item.save()
            return redirect('dashboard')
        else:
            return render(request, 'wanted_item/create.html', {'error': 'All fields are required', 'relief_center_id': relief_center_id})

    else:
        return render(request, 'wanted_item/create.html', {'relief_center_id': relief_center_id})

    return render(request, 'wanted_item/create.html', {'relief_center_id': relief_center_id})


@login_required(login_url="/accounts/signup")
def update(request, relief_center_id, wanted_item_id):
    relief_center = get_object_or_404(ReliefCenter, pk=relief_center_id)
    wanted_item = get_object_or_404(WantedItem, pk=wanted_item_id)
    print('Wanted Items in update' + str(wanted_item))
    if request.method == 'POST':
        if request.POST['name'] and request.POST['urgency_level'] and request.POST['description'] and request.POST['category'] and request.POST['quantity']:
            wanted_item.item_name = request.POST['name']
            wanted_item.urgency_level = request.POST['urgency_level']
            wanted_item.description = request.POST['description']
            wanted_item.category = request.POST['category']
            wanted_item.quantity = request.POST['quantity']
            wanted_item.relief_center_id = relief_center.id
            wanted_item.associated_relief_center = relief_center
            wanted_item.save()
            return redirect('dashboard')
        else:
            return render(request, 'wanted_item/update.html', {'error': 'All fields are required', 'relief_center_id': relief_center_id, 'wanted_item': wanted_item})

    else:
        return render(request, 'wanted_item/update.html', {'relief_center_id': relief_center_id, 'wanted_item': wanted_item})

    return render(request, 'wanted_item/update.html', {'relief_center_id': relief_center_id, 'wanted_item': wanted_item})


@login_required(login_url="/accounts/signup")
def delete(request, relief_center_id, wanted_item_id):
    wanted_item = get_object_or_404(WantedItem, pk=wanted_item_id)
    relief_center = get_object_or_404(ReliefCenter, pk=relief_center_id)
    print('Relief Center Id in delete is :' + str(relief_center.id))
    print('Wanted material.reliefcenterid in delete is:' +
          str(wanted_item.id))
    if request.method == 'POST':
        wanted_item.delete()
        return redirect('dashboard')

    else:
        return render(request, 'wanted_item/delete.html', {'relief_center_id': relief_center_id, 'wanted_item': wanted_item})
