from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

from bolo_flyers.models import Bolo
from bolo_users.models import Agency

def about(request):
    return render(request, 'bolo_app/about.html')

def contact(request):
    return render(request, 'bolo_app/contact.html')

@login_required
def dashboard(request):
    return render(request, 'bolo_app/dashboard.html')

@login_required
def profile(request):
    return render(request, 'bolo_app/profile.html')

class AgencyListView(LoginRequiredMixin, ListView):
    model = Agency
    template_name = 'bolo_app/agencies.html'
    context_object_name = 'agencies'

class AgencyDetailView(LoginRequiredMixin, DetailView):
    model = Agency
    template_name = 'bolo_app/agency_details.html'
    context_object_name = 'agency'
