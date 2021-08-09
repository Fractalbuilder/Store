# Generated by Django 3.1 on 2020-12-28 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201227_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='product',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='unitPrice',
        ),
        migrations.AddField(
            model_name='bill',
            name='accepted',
            field=models.CharField(default='false', max_length=5),
        ),
        migrations.AddField(
            model_name='bill',
            name='paid_for',
            field=models.CharField(default='false', max_length=5),
        ),
        migrations.AlterField(
            model_name='bill',
            name='totalPrice',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='leaf',
            field=models.CharField(max_length=5),
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unitPrice', models.FloatField()),
                ('totalPrice', models.FloatField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_detail_bill', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_detail_product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
