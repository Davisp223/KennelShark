# Generated by Django 3.2.4 on 2021-06-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0012_alter_entry_kennel'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='Checked_in',
            field=models.CharField(choices=[('Yes', 'Yes')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='Eve',
            field=models.CharField(blank=True, choices=[('X', 'X')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='Food_Location',
            field=models.CharField(blank=True, choices=[('A1', 'A1'), ('B2', 'B2'), ('C3', 'C3'), ('D4', 'D4'), ('E5', 'E5'), ('F6', 'F6'), ('G7', 'G7'), ('H8', 'H8'), ('I9', 'I9')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='Kennel',
            field=models.CharField(blank=True, choices=[('K1', 'K1'), ('K2', 'K2'), ('K3', 'K3'), ('DayCare', 'DayCare')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='Meds',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='Mrn',
            field=models.CharField(blank=True, choices=[('X', 'X')], max_length=40, null=True),
        ),
    ]
