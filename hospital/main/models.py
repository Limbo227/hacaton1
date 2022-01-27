from django.db import models
from django.shortcuts import render
# Create your models here.
from django.db import models
from django.urls import reverse


class Hospital(models.Model):
    title = models.CharField(verbose_name='title', max_length=200)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, verbose_name='region')
    okpo = models.IntegerField(verbose_name='ОКПО код', unique=True)

    def __str__(self):
        return self.title

class ChiefPhysician(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж Работы')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='masters')

    def __str__(self):
        return self.fio


class Doctor(models.Model):
    master_doctor = models.ForeignKey(ChiefPhysician, on_delete=models.CASCADE, verbose_name='master-doctor')
    directions = models.ForeignKey("DoctorType", on_delete=models.CASCADE, verbose_name='DoctorType')
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж Работы')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='doctors')


    def __str__(self):
        return self.fio


class Nurse(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    master_doctor = models.ForeignKey(ChiefPhysician, on_delete=models.CASCADE, verbose_name='master-doctor', related_name='nurse')
    her_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='her-doctor', related_name='nurse')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='nurse')

    def __str__(self):
        return self.fio



class Apatient(models.Model):
    treating_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='treating-doctor', related_name='td')
    treating_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, verbose_name='treating-nurse', related_name='tn')
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    disease = models.CharField(verbose_name='Причина', max_length=64)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='ap')

    def total_patients(self):
        total = Apatient.objects.count()
        return total

    def __str__(self):
        return self.fio




class DoctorType(models.Model):
    title = models.CharField(
        max_length=10,
        verbose_name='Doctor_type')

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(
        max_length=10,
        verbose_name='region')

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Название'
    verbose_name_plural = 'Названии'
    ordering = ['-title']




#####REGISTRATION AND AUTHORIZATION
