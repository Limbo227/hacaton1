from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from django.db.models import F
from .forms import UserRegistrationForm, UserLoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout



def index(request):
    hospitals = Hospital.objects.all()
    return render(request, template_name='main/index.html', context={'hospitals': hospitals})


def hospital_detail(request, title):
    hospital = Hospital.objects.get(title=title)
    hospitals = Hospital.objects.all()
    return render(request, template_name='main/hospital_detail.html', context={'hospital': hospital, 'hospitals': hospitals})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    return render(request, 'main/login.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



