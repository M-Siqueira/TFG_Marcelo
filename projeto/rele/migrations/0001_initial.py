# Generated by Django 3.0.4 on 2023-09-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Acionador ou Sensor', max_length=40, verbose_name='Descrição do relé')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Modelo')),
                ('ip', models.GenericIPAddressField(help_text='Por exemplo, 192.168.10.3 ou 10.20.10.2', verbose_name='Endereço IP do relé')),
                ('porta_logica', models.CharField(help_text='Por exemplo, 8081', max_length=5, verbose_name='Porta lógica do relé')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'rele',
                'verbose_name_plural': 'reles',
                'ordering': ['-is_active', 'marca', 'descricao'],
            },
        ),
    ]
