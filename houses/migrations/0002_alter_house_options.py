# Generated by Django 5.0 on 2023-12-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
    ]