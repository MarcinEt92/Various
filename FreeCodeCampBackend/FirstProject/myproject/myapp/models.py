from django.db import models

# Create your models here.


class Feature:
    id: int
    name: str
    details: str
    is_true: bool


class FeatureModel(models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=200)
    is_true = models.BooleanField()
