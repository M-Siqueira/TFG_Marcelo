# Generated by Django 3.0.4 on 2023-08-29 17:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comodo', '0004_comodo_equipamentos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuariocomodo', '0004_auto_20230829_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocomodo',
            name='lugar',
            field=models.CharField(choices=[('APARTAMENTO', 'Apartamento'), ('CASA', 'Casa'), ('CONSULTÓRIO', 'Consultório'), ('ESCRITÓRIO', 'Escritório'), ('SÍTIO', 'Sítio'), ('OUTRO', 'Outro')], max_length=12, null=True, verbose_name='Localização deste cômodo *'),
        ),
        migrations.AlterUniqueTogether(
            name='usuariocomodo',
            unique_together={('usuario', 'comodo', 'lugar', 'cidade')},
        ),
    ]
