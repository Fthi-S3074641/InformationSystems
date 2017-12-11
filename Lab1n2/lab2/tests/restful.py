import random

from lab2.models import Profile
from lab2.tests.base import BaseTest

BASE_URL = '/lab-two/restful/profiles/'


class RESTfulTest(BaseTest):
    def test_retrieve_all(self):
        result = self.client.get(BASE_URL)
        assert result.status_code == 200, f'Error: Result status code ' \
                                          f'{result.status_code}. {result.content}'

        data_check = [p.name for p in list(Profile.objects.all())]
        data_received = [p['name'] for p in result.data]

        assert all([name in data_received for name in data_check])

    def test_retrieve_one(self):
        random_profile = random.choice(list(Profile.objects.all()))
        result = self.client.get(f'{BASE_URL}{random_profile.id}/')
        assert result.status_code == 200, f'Error: Result status code ' \
                                          f'{result.status_code}. {result.content}'

        assert result.data['name'] == random_profile.name
