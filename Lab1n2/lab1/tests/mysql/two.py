import pickle
import random
import time

from django.test import TestCase

from InformationSystems.decorators import measure_total_time
from lab1.config import IMG_HEIGHT, IMG_WIDTH, NUM_IMAGES, NUM_QUERIES
from lab1.models.mysql.two import Image
from lab1.tests.misc import save_timeseries_plot


class SQLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(SQLTests, cls).setUpClass()
        cls.images = cls._create_images()

    @measure_total_time(NUM_QUERIES)
    def test_retrieve_image(self):
        res = [self._get_random_image() is not None for _ in range(0, NUM_QUERIES)]

        assert all(res)

    @measure_total_time(NUM_QUERIES)
    def test_retrieve_xy(self):
        res = []
        for _ in range(0, NUM_QUERIES):
            img = self._get_random_image()
            y = self._get_random_y(img)
            x = self._get_random_x(y)
            res.append(x is not None)

        assert all(res)

    @classmethod
    @measure_total_time(NUM_IMAGES)
    def _create_images(cls):
        ts_start = time.time()
        ts = [0]
        res = []
        for _ in range(0, NUM_IMAGES):
            res.append(Image.create())
            ts.append(time.time() - ts_start)

        save_timeseries_plot(ts)

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
        idx = random.randint(0, IMG_HEIGHT - 1)
        arr_int = pickle.loads(img.xy)
        return arr_int[idx]

    @staticmethod
    def _get_random_x(arr_int):
        idx_x = random.randint(0, IMG_WIDTH - 1)
        return arr_int[idx_x]
