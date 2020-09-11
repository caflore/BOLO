from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, CreateView
from django.shortcuts import render

from bolo_flyers.models import Bolo

@login_required
def bolos(request):
    return render(request, 'bolo_app/bolo.html')

def about(request):
    return render(request, 'bolo_app/about.html')

def contact(request):
    return render(request, 'bolo_app/contact.html')
