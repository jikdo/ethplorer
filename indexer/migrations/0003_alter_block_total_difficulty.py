# Generated by Django 3.2.8 on 2021-10-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0002_alter_block_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='total_difficulty',
            field=models.BigIntegerField(),
        ),
    ]