# Generated by Django 3.1 on 2020-12-28 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_cart_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totalPrice',
            field=models.FloatField(),
        ),
    ]
