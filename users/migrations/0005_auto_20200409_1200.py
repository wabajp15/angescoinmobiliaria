# Generated by Django 2.2.11 on 2020-04-09 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200409_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='type_identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Type_identity'),
        ),
    ]