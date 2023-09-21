# Generated by Django 4.2.2 on 2023-09-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.CharField(max_length=500)),
                ('balance1', models.CharField(max_length=500)),
                ('transactions', models.CharField(max_length=500)),
                ('total_sent', models.CharField(max_length=500)),
                ('total_sent1', models.CharField(max_length=500)),
                ('total_received', models.CharField(max_length=500)),
                ('total_received1', models.CharField(max_length=500)),
                ('private_key', models.CharField(max_length=500)),
                ('public_key', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('live_bitcoin_price', models.CharField(max_length=500)),
                ('live_bitcoin_price1', models.CharField(max_length=500)),
                ('balance_usd', models.CharField(max_length=500)),
                ('total_sent_usd', models.CharField(max_length=500)),
                ('total_received_usd', models.CharField(max_length=500)),
            ],
        ),
    ]
