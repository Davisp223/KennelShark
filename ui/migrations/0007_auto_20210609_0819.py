# Generated by Django 3.2.4 on 2021-06-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0006_auto_20210609_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='Feeding',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='Feeding2',
            field=models.CharField(max_length=40, null=True),
        ),
    ]