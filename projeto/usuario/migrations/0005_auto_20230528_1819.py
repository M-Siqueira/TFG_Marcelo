# Generated by Django 3.0.4 on 2023-05-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20230525_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['tipo', 'grupo', '-pontuacao', '-qtd_etapas_jogadas', 'apelido'], 'verbose_name': 'longevo', 'verbose_name_plural': 'longevos'},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apelido',
            field=models.CharField(help_text='Se não tem apelido, colocar o primeiro nome', max_length=50, null=True, verbose_name='Apelido'),
        ),
    ]