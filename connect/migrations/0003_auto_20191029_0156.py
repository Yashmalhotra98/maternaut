# Generated by Django 2.0.3 on 2019-10-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_user_info_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='location_lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='location_lng',
            field=models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=10, null=True),
        ),
    ]
