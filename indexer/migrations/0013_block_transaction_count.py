# Generated by Django 3.2.8 on 2021-11-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0012_auto_20211021_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='transaction_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
