from django.db import models

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
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, verbose_name='Бренд')
    automodel = models.ForeignKey(AutoModel, on_delete=models.CASCADE, verbose_name='Модель машины')
    body = models.ForeignKey(Body, on_delete=models.CASCADE, verbose_name='Тип кузова')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет кузова')
    ad_user = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Пользователь')
    year = models.IntegerField('Год выпуска')
    day = models.DateField('advert day')
    price = models.IntegerField()

    maker.admin_order_field = 'maker'

    def __str__(self):
        return str(self.day) + " " + str(self.price)


