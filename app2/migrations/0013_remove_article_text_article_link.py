# Generated by Django 4.1.7 on 2023-06-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0012_alter_track_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Text',
        ),
        migrations.AddField(
            model_name='article',
            name='Link',
            field=models.CharField(default='/', max_length=100),
            preserve_default=False,
        ),
    ]
