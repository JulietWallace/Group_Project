# Generated by Django 2.2 on 2024-03-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0010_auto_20240314_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='dateDay',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='dateMonth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='dateYear',
            field=models.IntegerField(null=True),
        ),
    ]
