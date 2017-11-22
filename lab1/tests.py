import random
import time

import math
from django.test import TestCase
import matplotlib.pyplot as plt

from InformationSystems.decorators import measure_total_time
from lab1.models import Image, RainXY

NUM_IMAGES = 37
NUM_QUERIES = 5000


class Lab1Test(TestCase):
    @classmethod
    @measure_total_time(1)
    def setUpClass(cls):
        super(Lab1Test, cls).setUpClass()
        cls.images = cls._create_images()

    @measure_total_time(NUM_QUERIES)
    def test_retrieve_image(self):
        res = [self._get_random_image() is not None for _ in range(0, NUM_QUERIES)]

        assert all(res)

    @measure_total_time(NUM_QUERIES)
    def test_retrieve_y(self):
        img = self._get_random_image()
        res = [self._get_random_y(img) is not None for _ in range(0, NUM_QUERIES)]

        assert all(res)

    @measure_total_time(NUM_QUERIES)
    def test_retrieve_xy(self):
        img = self._get_random_image()

        res = []
        for _ in range(0, NUM_QUERIES):
            y = self._get_random_y(img)
            x = self._get_random_x(y)
            res.append(x is not None)

        assert all(res)

    @classmethod
    def _create_images(cls):
        ts_start = time.time()
        ts = [0]
        res = []
        for _ in range(0, NUM_IMAGES):
            res.append(Image.create())
            ts.append(time.time() - ts_start)

        # cls._print_timeseries(ts)

        return res

    @classmethod
    def _get_random_image(cls):
        id_img = random.randint(1, NUM_IMAGES)
        try:
            return Image.objects.get(id=id_img)
        except Image.DoesNotExist:
            return cls._get_random_image()

    @classmethod
    def _get_random_y(cls, img):
        idx = random.randint(0, Image.HEIGHT - 1)
        try:
            return img.rainxy_set.get(y=idx)
        except RainXY.DoesNotExist:
            return cls._get_random_y(img)

    @staticmethod
    def _get_random_x(rainxy):
        idx_y = random.randint(0, Image.WIDTH - 1)
        arr = rainxy.x.split(',')
        return arr[idx_y]

    @staticmethod
    def _print_timeseries(ts):
        plt.plot(ts)
        plt.plot(ts, 'ro')
        plt.ylabel("Time since Start in Seconds")
        plt.xlabel("Number of Images created")
        plt.grid(True, axis='y', which='both')
        plt.yticks(range(0, math.ceil(max(ts))))
        plt.xticks(range(0, len(ts)))
        plt.show()

