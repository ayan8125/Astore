# Generated by Django 2.2.5 on 2019-09-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plumber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
