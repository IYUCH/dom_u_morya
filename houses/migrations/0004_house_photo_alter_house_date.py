# Generated by Django 5.0 on 2024-01-01 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_alter_house_options_house_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='фотография'),
        ),
        migrations.AlterField(
            model_name='house',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='дата'),
        ),
    ]
