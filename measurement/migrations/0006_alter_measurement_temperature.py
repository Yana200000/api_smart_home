# Generated by Django 4.0.2 on 2022-02-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
