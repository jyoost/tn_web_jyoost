# Generated by Django 3.0.7 on 2021-01-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicblog', '0005_auto_20210103_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicblogpage',
            name='middle_image_alt',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]
