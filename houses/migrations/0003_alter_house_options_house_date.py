# Generated by Django 5.0 on 2024-01-01 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_alter_house_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name'], 'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
        migrations.AddField(
            model_name='house',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='датта'),
        ),
    ]
