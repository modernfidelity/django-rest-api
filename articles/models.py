from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.


class Article(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', related_name='articles')



    # published_date = models.DateTimeField(
    #     blank=True, null=True)

    title = models.CharField(
        max_length=255,
    )

    strapline = models.CharField(
        max_length=255,
        default="",
    )

    body = models.TextField(
        default="",
    )

    def __str__(self):
        return self.title
