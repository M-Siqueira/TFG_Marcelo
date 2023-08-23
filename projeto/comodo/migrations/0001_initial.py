# Generated by Django 3.0.4 on 2023-08-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Quarto do pai ou Sala de estar.', max_length=50, verbose_name='Descrição do cômodo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'comodo',
                'verbose_name_plural': 'comodos',
                'ordering': ['descricao'],
            },
        ),
    ]