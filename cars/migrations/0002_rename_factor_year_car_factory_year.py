# Generated by Django 4.2.3 on 2023-07-26 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='factor_year',
            new_name='factory_year',
        ),
    ]
