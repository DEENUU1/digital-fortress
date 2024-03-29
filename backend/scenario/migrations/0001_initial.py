# Generated by Django 5.0.1 on 2024-02-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('limit_storage', models.FloatField(default=0)),
                ('current_storage', models.FloatField(default=0)),
                ('num_of_scenarios', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('user_details', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Scenario',
                'verbose_name_plural': 'Scenarios',
            },
        ),
    ]
