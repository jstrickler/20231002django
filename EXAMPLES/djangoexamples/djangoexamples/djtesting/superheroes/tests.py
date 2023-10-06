import sys
from unittest import skip, skipIf, skipUnless

from django.urls import reverse
from django.test import TestCase, tag

from superheroes.models import Superhero

class SuperheroTests(TestCase):

    fixtures = ['superheroes.json']

    # instance methods -- before and after each test
    def setUp(self):
        self.superman = Superhero.objects.get(name='Superman')

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    @skip('database not ready yet')
    def test_clark_kent_is_supermans_secret_identity(self):
        superman = Superhero.objects.get(name="Wonder Woman")
        self.assertEquals('Diana Prince', superman.secret_identity)

    @skipUnless(sys.platform == "win32", 'only runs on Windows')
    def test_supermans_real_name(self):
        superman = Superhero.objects.get(name="Superman")
        self.assertEquals('Kal-el', superman.real_name)

    @skipUnless(sys.platform == 'darwin', 'only runs on Mac')
    def test_response_returns_200(self):
        response = self.client.get(
            reverse('superheroes:herodetails', args=('Superman',))
        )
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(
            reverse('superheroes:herodetails', args=('Wonder Woman',))
        )
        self.assertTemplateUsed('superheroes/hero_details.html')

    @tag('slow')
    def test_result_contains_expected_data(self):
        response = self.client.get(
            reverse('superheroes:herodetails', args=('Superman',))
        )
        self.assertIn(b'Superman', response.content)

    @tag('silly')
    def test_two_plus_two_is_four(self):
        self.assertEqual(2 + 2, 4)
