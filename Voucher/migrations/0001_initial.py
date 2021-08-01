# Generated by Django 3.2.5 on 2021-08-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('code_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price_cut', models.PositiveSmallIntegerField()),
                ('minimum_price', models.IntegerField()),
                ('expired_date', models.DateField()),
            ],
        ),
    ]