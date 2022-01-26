from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.db.models import F



# Create your views here.

def index(request):
    return render(request, template_name='main/index.html')

# def bakai_hospital(request):
#     return render(request)

# def hospitals(request):
#     return render(request, template_name='main/hospitals.html')

class Hospitals(ListView):
    model = Hospital
    context_object_name = 'hospital'
    template_name = 'main/hospitals.html'






