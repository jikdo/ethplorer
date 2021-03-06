# Generated by Django 3.2.8 on 2021-10-21 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0007_rename_tokencontract_contract'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='hash',
            field=models.CharField(default=1, help_text='account address', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='block',
            name='miner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mined_blocks', to='indexer.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='from_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_transactions', to='indexer.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_transactions', to='indexer.account'),
        ),
    ]
