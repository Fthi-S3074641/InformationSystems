import random

from django.test import TestCase

# Create your tests here.
from InformationSystems.decorators import measure_performance
from lab1.models import Image

NUM_IMAGES = 12
NUM_QUERIES = 100000


class Lab1Test(TestCase):
    @classmethod
    @measure_performance(1)
    def setUpClass(cls):
        super(Lab1Test, cls).setUpClass()
        cls.images = [Image.create() for _ in range(0, NUM_IMAGES)]

    @measure_performance(NUM_QUERIES)
    def test_retrieve_image(self):
        res = [self.get_random_image() is not None for _ in range(0, NUM_QUERIES)]

        assert all(res)

    @measure_performance(NUM_QUERIES)
    def test_retrieve_x(self):
        img = self.get_random_image()
        x = self.get_random_x(img)

        assert x is not None

    @measure_performance(NUM_QUERIES)
    def test_retrieve_xy(self):
        img = self.get_random_image()
        x = self.get_random_x(img)
        y = self.get_random_y(x)

        assert y is not None

    @staticmethod
    def get_random_image():
        id_img = random.randint(1, NUM_IMAGES)
        return Image.objects.get(id=id_img)

    @staticmethod
    def get_random_x(img):
        idx_x = random.randint(1, Image.HEIGHT)
        return img.rainxy_set.get(x=idx_x)

    @staticmethod
    def get_random_y(rainxy):
        idx_y = random.randint(1, Image.WIDTH)
        arr = rainxy.y.split(',')
        return arr[idx_y]
