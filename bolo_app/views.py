from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bolo_flyers.models import Bolo

def about(request):
    return render(request, 'bolo_app/about.html')

def contact(request):
    return render(request, 'bolo_app/contact.html')

@login_required
def dashboard(request):
    return render(request, 'bolo_app/dashboard.html')
