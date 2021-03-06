# Generated by Django 3.1 on 2021-02-01 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='laptopFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=80)),
                ('ram', models.FloatField()),
                ('screenSize', models.FloatField()),
                ('storage', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_features_product', to='store.product')),
            ],
        ),
    ]
