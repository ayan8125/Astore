# Generated by Django 2.2.5 on 2019-10-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product_type',
            field=models.IntegerField(choices=[(0, 'perday'), (1, 'fullprocess')], max_length=50, null=True),
        ),
    ]