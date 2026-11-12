from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Product, Event
from .forms import EventForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shopping_list')
    else:
        form = UserCreationForm()

    return render(request, 'shopping_list/index.html', {'form': form, 'action': 'register'})


@login_required
def profile_view(request):
    user = request.user
    context = {
        'username': user.username,
        'date_joined': user.date_joined,
        'email': user.email,
        'action': 'profile'
    }
    return render(request, 'shopping_list/index.html', context)


@login_required
def shopping_list_view(request):
    products_to_buy = Product.objects.filter(is_bought=False)
    products_bought = Product.objects.filter(is_bought=True)

    context = {
        'to_buy': products_to_buy,
        'bought': products_bought,
        'count_remaining': products_to_buy.count(),
        'action': 'list'
    }
    return render(request, 'shopping_list/index.html', context)

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user).order_by('-date')
    return render(request, 'shopping_list/index.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'shopping_list/index.html', {'form': form, 'akcja': 'Dodaj'})

@login_required
def event_update(request, id):
    event = get_object_or_404(Event, id=id, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'shopping_list/index.html', {'form': form, 'akcja': 'Edytuj'})

@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id, user=request.user)
    if request.method == 'POST':
        event.delete()
    return redirect('event_list')