import datetime
import pickle

import mongoengine as mongo

from lab1.models.misc import gen_random_data


class Image(mongo.Document):
    timestamp = mongo.DateTimeField(default=datetime.datetime.utcnow())
    xy = mongo.BinaryField()

    @classmethod
    def create(cls):
        arr_int_2d = gen_random_data()
        arr_binary = pickle.dumps(arr_int_2d, protocol=2)
        return Image(xy=arr_binary).save()
