# Generated by Django 3.2.8 on 2021-10-21 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0010_alter_account_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='parent_hash',
        ),
        migrations.AddField(
            model_name='block',
            name='parent_block',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='indexer.block'),
        ),
    ]