# Generated by Django 3.2.4 on 2021-06-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0005_auto_20210608_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='qrcode',
        ),
        migrations.AlterField(
            model_name='entry',
            name='GCD',
            field=models.CharField(blank=True, default='BBN', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_groom',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_in',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_out',
            field=models.DateField(null=True),
        ),
    ]
