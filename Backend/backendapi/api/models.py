from django.db import models


class Book(models.Model):
    country = models.TextField(max_length=20, blank=False, null=False)
    infected = models.TextField(max_length=20, blank=False, null=False)
    recovered = models.TextField(max_length=20, blank=False, null=False)
    deaths = models.TextField(max_length=20, blank=False, null=False)
    lastUpdate = models.TextField(max_length=20, blank=False, null=False)

