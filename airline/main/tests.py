from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Aeroplane

# Create your tests here.

class AeroplaneModelTest(TestCase):
    '''Test Aeroplane Models'''
    
    def setUp(self):
        Aeroplane.objects.create(
                name='Boeing 737',
                id=5
            )
        Aeroplane.objects.create(
                name='Airbus A350',
                id=4
            )

    def test_aeroplane_instance(self):
        airbus = Aeroplane.objects.get(id='4')
        boeing = Aeroplane.objects.get(name='Boeing 737')
        self.assertEqual(airbus.id, 4)
        self.assertEqual(boeing.id, 5)
        self.assertEqual(boeing.__str__(), boeing.name)