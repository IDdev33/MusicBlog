# Generated by Django 4.1.7 on 2023-04-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_artist_full_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='Full_Article',
        ),
        migrations.AddField(
            model_name='artist',
            name='Facebook_Link',
            field=models.URLField(default='/', max_length=100),
        ),
        migrations.AddField(
            model_name='artist',
            name='Spotify_Link',
            field=models.URLField(default='/', max_length=100),
        ),
        migrations.AddField(
            model_name='artist',
            name='Twitter_Link',
            field=models.URLField(default='/', max_length=100),
        ),
        migrations.AddField(
            model_name='artist',
            name='Youtube_Video',
            field=models.URLField(default='/', max_length=100),
        ),
    ]