# Generated by Django 2.2.5 on 2019-10-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191007_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
