# Generated by Django 3.2.8 on 2021-12-08 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0015_alter_transaction_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='timestamp',
        ),
    ]