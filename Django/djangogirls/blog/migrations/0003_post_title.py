# Generated by Django 3.0.5 on 2020-04-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title Goes Here', max_length=200),
        ),
    ]