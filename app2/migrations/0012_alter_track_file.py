# Generated by Django 4.1.7 on 2023-06-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0011_article_track_delete_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='file',
            field=models.FileField(upload_to='tracks'),
        ),
    ]