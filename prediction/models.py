from django.db import models

# Create your models here.

CATEGORIES = [('1','First'),('2','Second')]

class MlModel(models.Model):
    likes = models.IntegerField()
    comments = models.IntegerField()   