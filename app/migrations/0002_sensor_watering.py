# Generated by Django 4.2.7 on 2023-11-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='watering',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]