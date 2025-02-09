# Generated by Django 5.0.6 on 2024-10-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midas', '0020_alter_symbol_broker_alter_symbol_exchange_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScannerRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('log', models.JSONField(verbose_name='Log')),
            ],
        ),
        migrations.RemoveField(
            model_name='scanner',
            name='strategy',
        ),
        migrations.AddField(
            model_name='scanner',
            name='algo',
            field=models.CharField(blank=True, choices=[('Panda', 'Panda'), ('Cat', 'Cat'), ('Coyote', 'Coyote')], null=True),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='leads',
            field=models.ManyToManyField(blank=True, related_name='scanner_leads', to='midas.symbol'),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='symbols',
            field=models.ManyToManyField(blank=True, related_name='scanner_symbols', to='midas.symbol', verbose_name='Watchlist'),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='time_frame',
            field=models.CharField(choices=[('Hour', 'Hour'), ('Day', 'Day'), ('Minute', 'Minute')], default='Hour'),
        ),
        migrations.AddField(
            model_name='scanner',
            name='runs',
            field=models.ManyToManyField(blank=True, related_name='scanner_runs', to='midas.scannerrun', verbose_name='ScannerRun'),
        ),
    ]
