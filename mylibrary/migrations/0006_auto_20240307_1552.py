# Generated by Django 2.2 on 2024-03-07 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0005_auto_20240307_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='books',
        ),
        migrations.AlterField(
            model_name='book',
            name='uploadedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.UserProfile'),
        ),
    ]
