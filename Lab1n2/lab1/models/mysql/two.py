import pickle

from django.db import models

from lab1.models.misc import gen_random_data


class Image(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    xy = models.BinaryField()

    @classmethod
    def create(cls):
        arr_int_2d = gen_random_data()
        arr_binary = pickle.dumps(arr_int_2d, protocol=2)
        return Image(xy=arr_binary).save()
