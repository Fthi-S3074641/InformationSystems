from django.test import TestCase
from faker import Faker
from rest_framework.test import APIClient

import lab2.config as config
from lab2.tests.misc import add_friends_to_profile, create_random_profile


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(TestCase, cls).setUpClass()
        cls.client = APIClient()
        cls.faker = Faker()

    def setUp(self):
        profiles = [create_random_profile() for _ in range(0, config.NUM_PROFILES)]
        [add_friends_to_profile(profile) for profile in profiles]
