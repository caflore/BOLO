from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'bolo_app/home.html')
