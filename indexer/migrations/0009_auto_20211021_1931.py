# Generated by Django 3.2.8 on 2021-10-21 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0008_auto_20211021_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='block_hash',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='block_number',
        ),
        migrations.AddField(
            model_name='transaction',
            name='block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='indexer.block'),
            preserve_default=False,
        ),
    ]
