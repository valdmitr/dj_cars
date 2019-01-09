from django.test import TestCase
from django.urls import reverse

from .models import Advert

class CarsIndexViewTests(TestCase):
    def test_no_cars(self):
        """
        If no cars exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('auto:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['ads'], [])
