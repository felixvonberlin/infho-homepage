# Generated by Django 5.0.2 on 2024-02-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postingstore',
            name='image_path_array',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_path_array',
            field=models.CharField(default='', max_length=4096),
        ),
    ]