# Generated by Django 3.0.4 on 2023-08-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0003_auto_20230822_1447'),
        ('comodo', '0003_auto_20230822_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='comodo',
            name='equipamentos',
            field=models.ManyToManyField(blank=True, help_text='Para selecionar ou deselecionar um equipamento pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse', null=True, related_name='equipamentos', to='equipamento.Equipamento', verbose_name='Equipamento(s)'),
        ),
    ]
