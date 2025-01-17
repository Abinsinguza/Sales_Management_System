# Generated by Django 5.1.4 on 2025-01-14 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffID', models.AutoField(primary_key=True, serialize=False)),
                ('staffName', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_id',
            new_name='shopID',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_name',
            new_name='shopName',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=255)),
                ('previousStockBalance', models.IntegerField()),
                ('datePreviousStockBalance', models.DateField()),
                ('currentStockBalance', models.IntegerField()),
                ('dateCurrentStockBalance', models.DateField(auto_now_add=True)),
                ('currentSockSupplied', models.IntegerField()),
                ('dateCurrentStockSupplied', models.DateField(auto_now_add=True)),
                ('previousStockSupplied', models.IntegerField()),
                ('datePreviousStockSupplied', models.DateField()),
                ('totalStockSupplied', models.IntegerField(default=0)),
                ('Unit', models.CharField(max_length=50)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.shop')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='staffAssigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.staff'),
        ),
    ]
