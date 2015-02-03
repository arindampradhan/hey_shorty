# from django.db import models

from redisco import models


class Url(models.Model):
    long_url = models.CharField(max_length=1000, required=True)
    short_url = models.CharField(max_length=5, required=True)
    created_at = models.DateTimeField(auto_now_add=True)
