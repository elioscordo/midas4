# Generated by Django 5.0.6 on 2024-10-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midas', '0012_indicatorinstance_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(blank=True, max_length=1023, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=1023, null=True, verbose_name='Name')),
            ],
        ),
        migrations.AlterField(
            model_name='indicatorinstance',
            name='setup',
            field=models.JSONField(blank=True, null=True, verbose_name='Setup'),
        ),
    ]
