import random

from django.core.validators import validate_comma_separated_integer_list
from django.db import models


# Create your models here.
class Image(models.Model):
    WIDTH = 550
    HEIGHT = 500



    @classmethod
    def create(cls):
        img = Image()
        img.save()

        arr2d = [[str(random.randint(0, 100)) for _ in range(cls.WIDTH)] for _ in range(cls.HEIGHT)]
        for idx in range(0, len(arr2d)):
            vals = ','.join(arr2d[idx])
            rain = RainXY(image=img, x=idx, y=vals)
            rain.save()

        return img


class RainXY(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.CharField(validators=[validate_comma_separated_integer_list],
                         max_length=Image.WIDTH * 4)
