from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from bolo_flyers.models import Bolo

class BoloListView(LoginRequiredMixin, ListView):
    model = Bolo
    template_name = 'bolo_flyers/bolos.html'
    context_object_name = 'bolos'
    ordering = ['-modified_date']

class BoloDetailView(LoginRequiredMixin, ListView):
    model = Bolo
    template_name = 'bolo_flyers/bolo_details.html'
    context_object_name = 'bolo'
    
