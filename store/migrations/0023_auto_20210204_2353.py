# Generated by Django 3.1 on 2021-02-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_datastoragefeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastoragefeature',
            name='storage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='desktopfeature',
            name='ram',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='desktopfeature',
            name='storage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laptopfeature',
            name='ram',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laptopfeature',
            name='storage',
            field=models.IntegerField(),
        ),
    ]
