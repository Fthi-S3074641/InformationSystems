import json
import random

import lab2.config as config
from lab2.models import Profile
from lab2.tests.base import BaseTest

BASE_URL = '/lab-two/graphql/'


class GraphQLTest(BaseTest):
    def test_retrieve_all(self):
        query = {'query': '''
                    query {
                        allProfiles {
                            name,
                            age, 
                            address,
                            friends {
                                name
                            }
                        }
                    }
                '''
                 }

        result = self.client.post(BASE_URL, data=query)
        assert result.status_code == 200, f'Error: Result status code ' \
                                          f'{result.status_code}. {result.content}'
        data = json.loads(result.content)['data']

        assert len(data['allProfiles']) == config.NUM_PROFILES

        profiles_retrieved = [p['name'] for p in data['allProfiles']]
        profiles_check = list(Profile.objects.all())

        assert all([p.name in profiles_retrieved for p in profiles_check])

    def test_retrieve_one(self):
        random_profile = random.choice(list(Profile.objects.all()))
        query = {'query': '''
                     query {
                        profile(id: ''' + str(random_profile.id) + ''') {
                            name
                        }
                    }
                    '''
                 }

        result = self.client.post(BASE_URL, data=query)
        assert result.status_code == 200, f'Error: Result status code ' \
                                          f'{result.status_code}. {result.content}'

        data = json.loads(result.content)['data']
        profile_retrieved = data['profile']

        assert profile_retrieved['name'] == random_profile.name
