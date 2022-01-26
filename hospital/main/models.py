from django.db import models

# Create your models here.
from django.db import models



class Hospital(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    Region = models.CharField(verbose_name='Регион Кыргызстана', max_length=200)
    okpo = models.IntegerField(verbose_name='ОКПО код', unique=True)


class ChiefPhysician(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж Работы')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='master')

class Doctor(models.Model):
    master_doctor = models.ForeignKey(ChiefPhysician, on_delete=models.CASCADE, verbose_name='master-doctor')
    directions = models.ForeignKey("DoctorType", on_delete=models.CASCADE, verbose_name='DoctorType')
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж Работы')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='doctor1')




class Nurse(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    master_doctor = models.ForeignKey(ChiefPhysician, on_delete=models.CASCADE, verbose_name='master-doctor', related_name='nurse')
    her_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='her-doctor', related_name='nurse')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='nurse')



class Apatient(models.Model):
    treating_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='treating-doctor', related_name='apatient')
    treating_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, verbose_name='treating-nurse', related_name='apatient')
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(verbose_name='Номер Телефона', max_length=64)
    disease = models.CharField(verbose_name='Причина', max_length=64)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='hospital', related_name='apatient')




class DoctorType(models.Model):
    title = models.CharField(
        max_length=10,
        verbose_name='Doctor_type')

class Meta:
    verbose_name = 'Название'
    verbose_name_plural = 'Названии'
    ordering = ['-title']


def __str__(self):
    return self.title