# Generated by Django 3.1 on 2020-12-27 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='name2',
        ),
    ]
