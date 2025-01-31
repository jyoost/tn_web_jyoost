# Generated by Django 3.2.5 on 2021-12-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UTM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.CharField(blank=True, max_length=100)),
                ('content', models.CharField(blank=True, max_length=100)),
                ('medium', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('term', models.CharField(blank=True, max_length=100)),
                ('aclk', models.BooleanField(blank=True, default=False)),
                ('fbclid', models.BooleanField(blank=True, default=False)),
                ('gclid', models.BooleanField(blank=True, default=False)),
                ('msclkid', models.BooleanField(blank=True, default=False)),
                ('twclid', models.BooleanField(blank=True, default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
