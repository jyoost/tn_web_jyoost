# Generated by Django 3.0.7 on 2021-01-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicBlogPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('topic', models.SlugField(allow_unicode=True)),
                ('body1_md', models.TextField()),
                ('body2_md', models.TextField()),
                ('body3_md', models.TextField()),
                ('template', models.CharField(max_length=80)),
                ('hero_image', models.CharField(max_length=100)),
                ('hero_text', models.CharField(max_length=80)),
                ('middle_image', models.CharField(max_length=100)),
                ('bullet_image_1', models.CharField(max_length=100)),
                ('bullet_text_1', models.TextField()),
                ('bullet_image_2', models.CharField(max_length=100)),
                ('bullet_text_2', models.TextField()),
                ('bullet_image_3', models.CharField(max_length=100)),
                ('bullet_text_3', models.TextField()),
                ('bullet_image_4', models.CharField(max_length=100)),
                ('bullet_text_4', models.TextField()),
                ('bullet_image_5', models.CharField(max_length=100)),
                ('bullet_text_5', models.TextField()),
                ('meta_description', models.TextField()),
                ('twitter_title', models.CharField(max_length=80)),
                ('twitter_description', models.TextField()),
                ('og_title', models.CharField(max_length=80)),
                ('og_description', models.TextField()),
            ],
        ),
    ]
