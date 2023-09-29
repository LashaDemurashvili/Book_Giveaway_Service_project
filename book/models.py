from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=50)
    genres = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)


