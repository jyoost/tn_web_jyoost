# Generated by Django 3.0.7 on 2021-08-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='more_address',
            field=models.CharField(blank=True, max_length=200, verbose_name="Complément d'adresse"),
        ),
    ]