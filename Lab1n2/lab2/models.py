from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.TextField()
    friends = models.ManyToManyField('self')
