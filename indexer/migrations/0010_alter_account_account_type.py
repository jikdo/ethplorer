# Generated by Django 3.2.8 on 2021-10-21 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0009_auto_20211021_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(max_length=42),
        ),
    ]
