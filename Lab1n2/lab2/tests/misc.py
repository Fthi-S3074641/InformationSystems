import random

from faker import Faker

import lab2.config as config
from lab2.models import Profile


def create_random_profile():
    faker = Faker()

    random_name = faker.name()
    random_age = random.randint(1, 100)
    random_address = faker.address()

    profile = Profile(name=random_name, age=random_age, address=random_address)
    profile.save()

    return profile


def add_friends_to_profile(profile):
    all_profiles = Profile.objects.all().exclude(id=profile.id)
    friends_to_add = random.sample(set(all_profiles), config.NUM_FRIENDS)
    [profile.friends.add(f) for f in friends_to_add]
