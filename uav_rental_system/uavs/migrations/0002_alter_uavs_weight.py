# Generated by Django 5.0.6 on 2024-05-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uavs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uavs',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
