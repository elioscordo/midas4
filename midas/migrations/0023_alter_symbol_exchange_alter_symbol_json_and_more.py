# Generated by Django 5.0.6 on 2024-10-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midas', '0022_alter_scanner_algo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='exchange',
            field=models.CharField(blank=True, null=True, verbose_name='Exchange'),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='json',
            field=models.JSONField(blank=True, max_length=1023, null=True, verbose_name='Json'),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='name',
            field=models.CharField(max_length=1023, null=True, verbose_name='Name'),
        ),
    ]
