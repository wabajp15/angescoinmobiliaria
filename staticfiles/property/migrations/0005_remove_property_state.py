# Generated by Django 2.2.11 on 2020-04-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_urlimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='state',
        ),
    ]
