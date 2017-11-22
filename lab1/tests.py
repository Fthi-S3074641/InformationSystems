import random

from django.test import TestCase

# Create your tests here.
from InformationSystems.decorators import measure_performance
from lab1.models import Image

NUM_IMAGES = 12


class Lab1Test(TestCase):
    @classmethod
    @measure_performance
    def setUpClass(cls):
        super(Lab1Test, cls).setUpClass()
        cls.images = [Image.create() for _ in range(0, NUM_IMAGES)]

    @measure_performance
    def test_retrieve_image(self):
        assert random.choice(self.images) is not None

    @measure_performance
    def test_retrieve_x(self):
        idx_x = random.randint(0, Image.HEIGHT)
        img = random.choice(self.images)
        val = img.rainxy_set.get(x=idx_x)
        assert val is not None

    @measure_performance
    def test_retrieve_xy(self):
        idx_x = random.randint(0, Image.HEIGHT)
        idx_y = random.randint(0, Image.WIDTH)
        img = random.choice(self.images)

        rainxy = img.rainxy_set.get(x=idx_x)
        arr = rainxy.y.split(',')
        val_y = arr[idx_y]

        assert val_y is not None
