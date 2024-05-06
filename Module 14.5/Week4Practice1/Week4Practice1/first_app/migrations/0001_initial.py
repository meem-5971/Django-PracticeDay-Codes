# Generated by Django 5.0.4 on 2024-05-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('roll', models.AutoField(primary_key=True, serialize=False)),
                ('registrant_id', models.BigIntegerField()),
                ('passed', models.BooleanField()),
                ('min_age', models.SmallIntegerField()),
                ('max_fees', models.BigIntegerField()),
                ('goals', models.TextField()),
            ],
        ),
    ]