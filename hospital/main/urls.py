from django.template.defaulttags import url
from django.urls import path
from .views import *
from django.conf.urls.static import static
from hospital import settings
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('hospitals/<str:title>', hospital_detail, name='hospital-detail'),
    path('author/', index, name='author'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


