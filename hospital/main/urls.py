from django.urls import path
from .views import *
from django.conf.urls.static import static
from hospital import settings

urlpatterns = [
    path('', index)
]