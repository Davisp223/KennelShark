# Generated by Django 3.2.4 on 2021-06-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0014_alter_entry_checked_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='Checked_in',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], default='No', max_length=25, null=True),
        ),
    ]
