"""
URL configuration for shopping_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from shopping_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shopping_list_view, name='shopping_list'),
    path('buy/<int:id>/', views.product_buy, name='product_buy'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='shopping_list/index.html',
        extra_context={'action': 'login'}
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
