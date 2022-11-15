# Generated by Django 3.2.16 on 2022-11-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_auto_20221108_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlmodel',
            name='category',
            field=models.CharField(choices=[('Soccer-International', 'Soccer-International'), ('Soccer-Highlights', 'Soccer-Highlights'), ('Soccer-LaLiga', 'Soccer-LaLiga'), ('Soccer-SerieA', 'Soccer-SerieA'), ('Basketball-Highlights', 'Basketball-Highlights'), ('Basketball-NBA', 'Basketball-NBA'), ('Basketball-Highlights', 'Basketball-Highlights'), ('Fighting-Highlights', 'Fighting-Highlights'), ('Fighting-UFC', 'Fighting-UFC'), ('Fighting-WWE', 'Fighting-WWE'), ('Racing-Formula 1', 'Racing-Formula 1'), ('Racing-Formula 2', 'Racing-Formula 2'), ('Racing-MotoGP', 'Racing-MotoGP'), ('Racing-Highlights', 'Racing-Highlights'), ('Racing-Son Viraj', 'Racing-Son Viraj'), ('Betting', 'Betting'), ('Tennis-Highlights', 'Tennis-Highlights'), ('Tennis-Wimbledon', 'Tennis-Wimbledon'), ('Tennis-ATP', 'Tennis-ATP')], default='Soccer-International', max_length=30),
        ),
        migrations.AlterField(
            model_name='mlmodel',
            name='year',
            field=models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], default='2022', max_length=5),
        ),
    ]