# Generated by Django 3.2.5 on 2021-10-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicblog', '0011_topicblogtemplate_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicblogitem',
            name='item_type',
            field=models.CharField(choices=[('---------', '---------'), ('article', 'article'), ('project', 'project'), ('press_release', 'press_release'), ('newsletter', 'newsletter'), ('newsletter_web', 'newsletter_web'), ('petition', 'petition'), ('mailing_list_signup', 'mailing_list_signup')], default='---------', max_length=100),
        ),
    ]