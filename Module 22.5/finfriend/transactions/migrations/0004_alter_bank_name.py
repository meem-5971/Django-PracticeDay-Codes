# Generated by Django 5.0.4 on 2024-06-19 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_bank_transactions_receiver_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(blank=True, default='bankrupt', max_length=200, null=True),
        ),
    ]
