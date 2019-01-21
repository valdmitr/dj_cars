import copy
import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.core import management

from .models import Advert, Maker, AutoModel, Color, Body
from .forms import PostForm


def setUpModule():
    """
    переопределяем setUpModule
    """
    management.call_command('loaddata', 'data_for_test_form.json', verbosity=0)


form_data = {
    'maker': 1,
    'automodel': 1,
    'body': 1,
    'color': 1,
    'year': 2018,
    'price': 1,
    'phone': '+79998887766',
    'status': True,
}


def create_advert():
    """
    функция для создания объявления, которое потом должно попасть в QuerySet.
    """
    maker = Maker.objects.create(name="Audi")
    automodel = AutoModel.objects.create(name="A4")
    body = Body.objects.create(name="седан")
    color = Color.objects.create(name="черный")
    ad_user = User.objects.create(username="Bob")
    day = '2018-12-29'
    price = 1

    return Advert.objects.create(maker=maker, automodel=automodel, body=body,
                                 color=color, ad_user=ad_user, year=2010,
                                 day=day, pic=None, phone="1",
                                 price=price, status=True)


class CarsIndexViewTests(TestCase):
    """
    Тестируем страницу index.
    """
    def test_no_cars(self):
        """
        If no cars exist, message is displayed.
        """
        response = self.client.get(reverse('auto:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['ads'], [])

    def test_status_true(self):
        """
        If status=True, advert display.
        """
        create_advert()
        response = self.client.get(reverse('auto:index'))
        self.assertQuerysetEqual(response.context['ads'],
                                 ['<Advert: 2018-12-29 1>'])


class AddPostTests(TestCase):
    """
    Тест формы PostForm.
    """
    def test_true_forms(self):
        """
        Форма PostForm валидна.
        """
        ad_user = User.objects.create(username="Bob")
        day = datetime.datetime.now()
        my_data = copy.deepcopy(form_data)
        my_data.update({'ad_user': ad_user, 'day': day})
        print(my_data)
        form = PostForm(data=my_data)
        form.is_valid()
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_forms_min_price(self):
        """
        Если цена отрицательная, форма PostForm не валидна.
        """
        ad_user = User.objects.create(username="Bob")
        day = datetime.datetime.now()
        my_data = copy.deepcopy(form_data)
        my_data.update({'ad_user': ad_user, 'day': day, 'price': -1})
        form = PostForm(data=my_data)
        form.is_valid()
        self.assertFalse(form.is_valid())

    def test_forms_old_year(self):
        """
        Если год выпуска меньше 1900, форма PostForm не валидна.
        """
        ad_user = User.objects.create(username="Bob")
        day = datetime.datetime.now()
        my_data = copy.deepcopy(form_data)
        my_data.update({'ad_user': ad_user, 'day': day, 'year': 1899})
        form = PostForm(data=my_data)
        form.is_valid()
        self.assertFalse(form.is_valid())

    def test_forms_future_year(self):
        """
        Если год больше текущего, то форма PostForm не валидна.
        """
        ad_user = User.objects.create(username="Bob")
        day = datetime.datetime.now()
        my_data = copy.deepcopy(form_data)
        my_data.update({'ad_user': ad_user, 'day': day, 'year': day.year + 1})
        form = PostForm(data=my_data)
        form.is_valid()
        self.assertFalse(form.is_valid())
