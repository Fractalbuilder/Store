# Generated by Django 3.1 on 2020-12-28 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201228_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetail',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_detail_bill', to='store.bill'),
        ),
        migrations.AlterField(
            model_name='billdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_detail_product', to='store.product'),
        ),
    ]
