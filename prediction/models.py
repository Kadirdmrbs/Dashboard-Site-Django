from django.db import models

# Create your models here.

Category_Choices = (
    ('Basketball','BASKETBALL'),
    ('Betting', 'BETTING'),
    ('Fighting','FIGHTING'),
    ('Racing','RACING'),
    ('Soccer','SOCCER'),
    ('Tennis','TENNIS')
)

Year_Choices = (
    ('2018','2018'),
    ('2019', '2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022')
)

class MlModel(models.Model):
    likes = models.IntegerField()
    comments = models.IntegerField()
    duration = models.IntegerField()
    category = models.CharField(max_length=15,choices=Category_Choices, default='Basketball')
    year = models.CharField(max_length=5,choices=Year_Choices, default='2021')