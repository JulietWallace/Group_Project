# Generated by Django 2.2.28 on 2024-03-22 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0002_auto_20240322_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='dateDue',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 13, 18, 11, 955205)),
        ),
    ]
