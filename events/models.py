from __future__ import unicode_literals

from datetime import datetime

from django.db import models


# Create your models here.


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    # owner = models.ForeignKey('auth.User', related_name='events', default="admin")

    title = models.CharField(
        max_length=255,
    )

    date_start = models.DateField('date start', default=datetime.today)

    date_end = models.DateField('date end')

    strapline = models.TextField(
        default="",
    )

    image = models.ImageField(upload_to='events/', default='events/none/default.jpg')

    body = models.TextField(
        default="",
    )

    #
    def img_thumb(self):
        """
        Handles the thumbnail for the admin list views
        Returns:

        """
        return u'<img width="75px" src="%s" />' % self.image.url

    img_thumb.short_description = 'Image'
    img_thumb.allow_tags = True

    #
    def __str__(self):
        """

        Returns:

        """
        return self.title
