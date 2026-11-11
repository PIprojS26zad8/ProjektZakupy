from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Product


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shopping_list')
    else:
        form = UserCreationForm()

    # Przekazujemy action: 'register'
    return render(request, 'shopping_list/index.html', {'form': form, 'action': 'register'})


@login_required
def profile_view(request):
    user = request.user
    # Przekazujemy action: 'profile'
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

    # Przekazujemy action: 'list' (lub zostawiamy domyślnie, w HTML 'else' to wyłapie)
    context = {
        'to_buy': products_to_buy,
        'bought': products_bought,
        'count_remaining': products_to_buy.count(),
        'action': 'list'
    }
    return render(request, 'shopping_list/index.html', context)