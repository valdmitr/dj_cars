import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.contrib import auth

User

class Maker(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class AutoModel(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class MakerAndModel(models.Model):
    model = models.ForeignKey(AutoModel, on_delete=models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)


class Body(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Advert(models.Model):
    maker = models.ForeignKey(
        Maker, on_delete=models.CASCADE, verbose_name='Бренд'
    )
    automodel = models.ForeignKey(AutoModel, on_delete=models.CASCADE,
                                  verbose_name='Модель машины')
    body = models.ForeignKey(Body, on_delete=models.CASCADE,
                             verbose_name='Тип кузова')
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              verbose_name='Цвет кузова')
    ad_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    year = models.IntegerField('Год выпуска')
    day = models.DateField('advert day')
    price = models.IntegerField()
    pic = models.ImageField(
        upload_to='user_pic', max_length=255, blank=True, null=True
    )
    phone = models.CharField(max_length=13, blank=True, null=True)
    status = models.BooleanField(verbose_name="Активно ли объявление", default=True)


    def get_maker(self):
        return  self.maker
    get_maker.admin_order_field = 'maker__name'

    def get_model(self):
        return  self.automodel
    get_model.admin_order_field = 'automodel__name'

    def is_now(self):
        return datetime.date.today() - datetime.timedelta(days=7) <= self.day




    def __str__(self):
        return str(self.day) + " " + str(self.price)


