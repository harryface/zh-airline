import math
# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.serializers import AeroplaneSerializer


# Create your tests here.


class AeroplaneAPITestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.aeroplane_url = reverse('aeroplane')

    def test_single_post_verify_output(self):
        # Prepare Data
        aeroplane_dict = {
            "id": 2,
            "name": "Airbus A350",
            "passenger": 2
        }
        # Make request
        response = self.client.post(self.aeroplane_url, aeroplane_dict)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check computed data
        self.assertEqual(
            response.data['passenger'], 2)
        self.assertEqual(
            response.data['total_fuel_consumption_per_minute'], 0.5585177444479562)
        self.assertEqual(
            response.data['max_minute_able_to_fly'], 716.1813639338594)

    def test_multiple_post_verify_output(self):
        # Prepare Data
        aeroplane_dict = [
            {
                "id": 2,
                "name": "Airbus A350",
                "passenger": 2
            },
            {
                "id": 1,
                "name": "Airbus A350",
                "passenger": 20
            }
        ]
        # Make request
        response = self.client.post(self.aeroplane_url, aeroplane_dict)
        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for aeroplane in response.data:

            consumption = (
                math.log(aeroplane['id']) * 0.8) + (aeroplane['passenger'] * 0.002)
            max_min_to_fly = (aeroplane['id'] * 200) / consumption

            self.assertEqual(
                aeroplane['max_minute_able_to_fly'], max_min_to_fly)
            self.assertEqual(
                aeroplane['total_fuel_consumption_per_minute'], consumption)
            self.assertEqual(
                aeroplane['id'], aeroplane['id'])
