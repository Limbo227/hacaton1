from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, template_name='main/index.html')

# def bakai_hospital(request):
#     return render(request)
