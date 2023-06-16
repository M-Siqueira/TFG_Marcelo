# Generated by Django 3.0.4 on 2023-06-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etapa', '0005_etapa_inscricoes_abertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='inscricoes_abertas',
            field=models.BooleanField(default=True, help_text='Desmarque o campo para encerrar as inscrições.', verbose_name='Etapa com inscrições abertas'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Se ativo, a etapa pode ter inscrições', verbose_name='Ativo'),
        ),
    ]
