from django.db import models


# Create your models here.

class Page(models.Model):
    comment = models.CharField(max_length=200, default=None)
    like = models.IntegerField(default=0, null=True)
    video_id = models.CharField(max_length=50, default=None)
