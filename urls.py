"""
URL configuration for crypto_dapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from crypto import views 
from crypto.views import signup_view, login_view, profile_view, dashboard_view
from django.contrib.auth import views as auth_views
from crypto.views import signup, CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Authentication using django-allauth (optional, if you need other auth functionality)
    path('auth/', include('allauth.urls')),  # Keep or remove based on your needs
    path('accounts/', include('allauth.urls')),
    
    # Main views
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('convert/', views.convert, name='convert'),
    path('converter/', views.converter, name='converter'),
    
    # Authentication views
    path('', signup_view, name='signup'),  # Ensure you're using one signup view
    path('login/', CustomLoginView.as_view(), name='login'),  # Login using CustomLoginView
    
    # Profile view
    path('profile/', views.profile_view, name='profile'),

    # Transaction views
    path('save_transaction/', views.save_transaction, name='save_transaction'),
    
    # Authentication logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

]




