# Generated by Django 3.0.4 on 2023-09-14 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rele', '0001_initial'),
        ('equipamento', '0004_auto_20230823_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='rele',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rele', to='rele.Rele', verbose_name='Relé associado ao equipamento'),
        ),
    ]
