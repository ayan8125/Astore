# Generated by Django 2.2.5 on 2019-10-08 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0002_auto_20191007_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='hire_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
