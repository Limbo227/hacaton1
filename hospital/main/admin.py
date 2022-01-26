from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Hospital)
admin.site.register(ChiefPhysician)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Apatient)
admin.site.register(DoctorType)