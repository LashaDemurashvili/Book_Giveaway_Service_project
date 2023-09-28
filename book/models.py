from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
