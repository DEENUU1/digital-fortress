# Generated by Django 5.0.1 on 2024-02-23 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=3)),
                ('price_id', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Product price',
                'verbose_name_plural': 'Product prices',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('max_project_storage', models.PositiveIntegerField()),
                ('num_of_projects', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_free', models.BooleanField(default=False)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.productprice')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('expiration_date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.product')),
            ],
            options={
                'verbose_name': 'User subscription',
                'verbose_name_plural': 'User subscriptions',
            },
        ),
    ]
