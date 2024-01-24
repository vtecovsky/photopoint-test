from django.contrib.auth.models import AbstractUser
from django.db import models


class CurrencyHistory(models.Model):
    usd = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
