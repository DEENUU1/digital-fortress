# Generated by Django 5.0.1 on 2024-02-03 10:50

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
                ('billing_cycle', models.CharField(choices=[('1', 'monthly'), ('2', 'life time')], max_length=2)),
            ],
            options={
                'verbose_name': 'Product price',
                'verbose_name_plural': 'Product prices',
            },
        ),
    ]