# Generated by Django 2.2.5 on 2019-10-26 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orders_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='employee',
        ),
    ]
