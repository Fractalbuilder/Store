# Generated by Django 3.1 on 2020-12-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201227_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='leaf',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]
