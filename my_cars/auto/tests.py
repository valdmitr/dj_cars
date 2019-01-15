from unittest import TestCase

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Advert, Maker, AutoModel, Color, Body


def create_advert(status):
    maker = Maker.objects.create(name="Audi")
    automodel = AutoModel.objects.create(name="A4")
    body = Body.objects.create(name="седан")
    color = Color.objects.create(name="черный")
    ad_user = User.objects.create(username="Bob")

    return Advert.objects.create(maker=maker, automodel=automodel, body=body, color=color,
                                 ad_user=ad_user, year=2010,
                                 day='2018-12-29', pic=None, phone="1",
                                 price=1, status=status)



class CarsIndexViewTests(TestCase):


    def test_no_cars(self):
        """
        If no cars exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('auto:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['ads'], [])

    def test_status_true(self):
        """
        If status=True, advert display.
        """
        create_advert(status=True)
        response = self.client.get(reverse('auto:index'))
        self.assertQuerysetEqual(response.context['ads'],
                                 ['<Advert: 2018-12-29 1>'])

    def test_status_false(self):
        """
        If status=False, advert doesn't display.
        """
        create_advert(status=False)
        response = self.client.get(reverse('auto:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['ads'], [])


#
# class TestDetail(TestCase):
#     pass
