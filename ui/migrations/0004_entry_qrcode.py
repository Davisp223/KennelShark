# Generated by Django 3.2.4 on 2021-06-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0003_auto_20210607_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='qrcode',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]