# Generated by Django 3.0.4 on 2023-05-28 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etapa', '0003_etapa_grupo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etapa',
            options={'ordering': ['grupo', '-data'], 'verbose_name': 'etapa', 'verbose_name_plural': 'etapas'},
        ),
    ]