from django.urls import path
from .views import *
from django.conf.urls.static import static
from hospital import settings
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    # path('aziz-hospital/', aziz_hospital, name='aziz-hospital')
    # path('bakai-hospital/', bakai_hospital, name='bakai-hospital')
    # path('elmara-hospital/', elmara_hospital, name='elmara-hospital')

]