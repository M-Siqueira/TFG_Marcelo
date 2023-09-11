# Generated by Django 3.0.4 on 2023-09-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuariocomodo', '0007_auto_20230830_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariocomodo',
            name='inverno_climatizacao_manha',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Manhã'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='inverno_climatizacao_noite',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='inverno_climatizacao_tarde',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='outono_climatizacao_manha',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Manhã'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='outono_climatizacao_noite',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='outono_climatizacao_tarde',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='primavera_climatizacao_manha',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Manhã'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='primavera_climatizacao_noite',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='primavera_climatizacao_tarde',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='verao_climatizacao_manha',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Manhã: '),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='verao_climatizacao_noite',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AddField(
            model_name='usuariocomodo',
            name='verao_climatizacao_tarde',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('MÉDIA', 'Média'), ('BAIXA', 'Baixa'), ('DESLIGADA', 'Desligada')], default='MÉDIA', help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='inverno_iluminacao_manha',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Manhã'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='inverno_iluminacao_noite',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='inverno_iluminacao_tarde',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='outono_iluminacao_manha',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Manhã'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='outono_iluminacao_noite',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='outono_iluminacao_tarde',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='primavera_iluminacao_manha',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Manhã'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='primavera_iluminacao_noite',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='primavera_iluminacao_tarde',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Tarde'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='verao_iluminacao_manha',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Manhã: '),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='verao_iluminacao_noite',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Noite'),
        ),
        migrations.AlterField(
            model_name='usuariocomodo',
            name='verao_iluminacao_tarde',
            field=models.CharField(blank=True, choices=[('FORTE', 'Forte'), ('MÉDIA', 'Médio'), ('FRACA', 'Fraco'), ('DESLIGADA', 'Desligada')], help_text='Itensidade da iluminação', max_length=10, null=True, verbose_name='Tarde'),
        ),
    ]
