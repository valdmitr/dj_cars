from django.db import models

class Maker(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AutoModel(models.Model):
    name = models.CharField(max_length=20)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    automodel = models.ForeignKey(AutoModel, on_delete=models.CASCADE)
    body = models.ForeignKey(Body, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    ad_user = models.ForeignKey(Person, on_delete=models.CASCADE)
    year = models.IntegerField()
    day = models.DateField('advert day')
    price = models.IntegerField()

    def __str__(self):
        return self.day + " " + self.price


