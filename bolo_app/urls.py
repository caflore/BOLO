"""BOLO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.contrib.auth import views as auth_views

from bolo_app.views import AgencyListView, AgencyDetailView
from bolo_app import views

urlpatterns = [
    path('', views.dashboard),
    path('login/', auth_views.LoginView.as_view(template_name='bolo_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bolo_app/logout.html'), name='logout'),
    path('about/', views.about, name='bolo-about'),
    path('contact/', views.contact, name='bolo-contact'),
    path('dashboard/', views.dashboard, name='bolo-dash'),
    path('agencies/', AgencyListView.as_view(), name='bolo-agencies'),
    path('agencies/<pk>', AgencyDetailView.as_view(), name='bolo-agency-detail'),
]
