# Generated by Django 3.2.3 on 2022-02-09 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='Videos/original/%Y/%m/%d')),
                ('video_240', models.FileField(upload_to='Videos/240p/%Y/%m/%d')),
                ('video_360', models.FileField(upload_to='Videos/360p/%Y/%m/%d')),
                ('percent', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]