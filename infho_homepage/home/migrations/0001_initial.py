# Generated by Django 5.0.2 on 2024-02-28 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostingStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('title', models.CharField(max_length=128)),
                ('title_image_path', models.CharField(max_length=512)),
                ('image_path_array', models.CharField(max_length=4096)),
                ('content_text', models.CharField(max_length=16384)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('postingstore_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.postingstore')),
            ],
            bases=('home.postingstore',),
        ),
        migrations.CreateModel(
            name='InfoPost',
            fields=[
                ('postingstore_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.postingstore')),
            ],
            bases=('home.postingstore',),
        ),
    ]