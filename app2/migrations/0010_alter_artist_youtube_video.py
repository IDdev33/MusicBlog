# Generated by Django 4.1.7 on 2023-04-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0009_alter_artist_youtube_channel_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='Youtube_Video',
            field=models.URLField(default='/', max_length=100),
        ),
    ]
