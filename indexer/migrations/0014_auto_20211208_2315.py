# Generated by Django 3.2.8 on 2021-12-08 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0013_block_transaction_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='max_fee_per_gas',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='max_priority_fee_per_gas',
        ),
    ]