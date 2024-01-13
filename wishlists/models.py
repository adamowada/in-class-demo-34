from django.db import models
from django.contrib.auth import get_user_model


class Wishlist(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    things = models.ManyToManyField('things.Thing', blank=True)

    def __str__(self):
        return f"{self.owner}'s Wishlist"
