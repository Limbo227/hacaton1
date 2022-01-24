from django.db import models

# Create your models here.
from django.db import models



class BonLitsa(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    Region = models.CharField(verbose_name='Регион Кыргызстана', max_length=200)
    okpo = models.IntegerField(verbose_name='ОКПО код')


class ChiefPhysician(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж Работы')
    phone_number = models.IntegerField(verbose_name='Номер Телефона')


class Doctor(models.Model):
    directions = models.ForeignKey("Doctors", on_delete=models.DO_NOTHING, verbose_name='Doctor')
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    work_experience = models.IntegerField(verbose_name='Стаж Работы')
    phone_number = models.IntegerField(verbose_name='Номер Телефона')


class Nurse(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.IntegerField(verbose_name='Номер Телефона')


class Apatient(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О', max_length=200)
    passport = models.CharField(verbose_name='ПИН-КОД паспорта', max_length=64)
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.IntegerField(verbose_name='Номер Телефона')
    disease = models.CharField(verbose_name='Причина обращения в больницу', max_length=64)


class Doctors(models.Model):
    title = models.CharField(
        max_length=10,
        verbose_name='Doctors')