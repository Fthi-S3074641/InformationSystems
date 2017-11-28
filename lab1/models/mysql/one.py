from django.core.validators import validate_comma_separated_integer_list
from django.db import models

from lab1.config import IMG_HEIGHT, IMG_WIDTH
from lab1.models.misc import gen_random_val


class Image(models.Model):
    timestamp = models.DateField(auto_now_add=True)

    @classmethod
    def create(cls):
        img = Image()
        img.save()

        arr2d = [[str(gen_random_val()) for _ in range(IMG_WIDTH)] for _ in
                 range(IMG_HEIGHT)]
        for idx, vals in enumerate(arr2d):
            vals = ','.join(vals)
            rain = RainXY(image=img, y=idx, x=vals)
            rain.save()

        return img


class RainXY(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    y = models.IntegerField()
    x = models.TextField(validators=[validate_comma_separated_integer_list])
