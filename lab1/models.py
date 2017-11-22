import random

from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class Image(models.Model):
    WIDTH = 550
    HEIGHT = 500

    SCARCITY = 30

    timestamp = models.DateField(auto_now_add=True)

    @classmethod
    def create(cls):
        img = Image()
        img.save()

        arr2d = [[str(cls.gen_random_rain()) for _ in range(cls.WIDTH)] for _ in range(cls.HEIGHT)]
        for idx in range(0, len(arr2d)):
            vals = ','.join(arr2d[idx])
            rain = RainXY(image=img, y=idx, x=vals)
            rain.save()

        return img

    @classmethod
    def gen_random_rain(cls):
        val = random.randint(0, 100)
        return val if val > cls.SCARCITY else 0


class RainXY(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    y = models.IntegerField()
    x = models.CharField(validators=[validate_comma_separated_integer_list],
                         max_length=Image.WIDTH * 4)
