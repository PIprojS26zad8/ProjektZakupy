from django.shortcuts import render, redirect, get_object_or_404
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
def shopping_list_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        if product_name:
            Product.objects.create(name=product_name, is_bought=False, user=request.user)
        return redirect('shopping_list')

        products_to_buy = Product.objects.filter(is_bought=False, user=request.user)
        products_bought = Product.objects.filter(is_bought=True, user=request.user)

    context = {
        'to_buy': products_to_buy,
        'bought': products_bought,
        'count_remaining': products_to_buy.count(),
        'action': 'list'
    }
    return render(request, 'shopping_list/index.html', context)


@login_required
def product_buy(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id, user=request.user)
        product.is_bought = True
        product.save()
    return redirect('shopping_list')

@login_required
def product_delete(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id, user=request.user)
        product.delete()
    return redirect('shopping_list')