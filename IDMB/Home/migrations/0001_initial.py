# Generated by Django 3.2.6 on 2021-08-26 09:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField(default=datetime.datetime.now, verbose_name='Date of birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('language', models.CharField(max_length=100)),
                ('length', models.DecimalField(decimal_places=2, max_digits=3)),
                ('avg_rating', models.FloatField(default=0)),
                ('artist', models.ManyToManyField(blank=True, to='Home.Artist')),
                ('awards_received', models.ManyToManyField(blank=True, to='Home.Awards')),
            ],
        ),
     
    ]
