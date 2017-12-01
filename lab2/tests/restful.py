import random

from django.test import TestCase
from faker import Faker
from rest_framework.test import APIRequestFactory

import lab2.config as config
from lab2.models import Profile


class RESTfulTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(RESTfulTest, cls).setUpClass()
        cls.factory = APIRequestFactory()
        cls.faker = Faker()

    def setUp(self):
        profiles = [self._create_random_profile() for _ in range(0, config.NUM_PROFILES)]
        [self._add_friends_to_profile(profile) for profile in profiles]

    def test_retrieve_all(self):
        result = self.factory.get('lab2/restful/profiles')
        print(result)

    def _create_random_profile(self):
        random_name = self.faker.name()
        random_age = random.randint(1, 100)
        random_address = self.faker.address()

        return Profile(name=random_name, age=random_age, address=random_address)

    def _add_friends_to_profile(self, profile):
        all_profiles = Profile.objects.all().exclude(id=profile.id)
        friends_to_add = random.sample(all_profiles, config.NUM_FRIENDS)
        [profile.friends.add(f) for f in friends_to_add]
