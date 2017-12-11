import datetime

import mongoengine as mongo

from lab1.models.misc import gen_random_data


class Image(mongo.Document):
    timestamp = mongo.DateTimeField(default=datetime.datetime.utcnow())

    @classmethod
    def create(cls):
        img = Image().save()
        arr2d = gen_random_data()

        for idx, vals in enumerate(arr2d):
            rain = RainXY(image=img, y=idx, x=vals).save()

        return img


class RainXY(mongo.Document):
    image = mongo.ReferenceField(Image, reverse_delete_rule=mongo.CASCADE)
    y = mongo.IntField()
    x = mongo.ListField(mongo.IntField())
