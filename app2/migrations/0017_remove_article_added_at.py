# Generated by Django 3.2.1 on 2024-01-12 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0016_delete_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Added_at',
        ),
    ]
