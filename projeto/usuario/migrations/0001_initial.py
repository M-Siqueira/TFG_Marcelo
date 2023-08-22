# Generated by Django 3.0.4 on 2023-08-22 16:45

import django.contrib.auth.models
from django.db import migrations, models
import usuario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('ORDINÁRIO', 'Ordinário')], default='ATLETA', help_text='* Campos obrigatórios', max_length=15, verbose_name='Tipo do usuário *')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo *')),
                ('celular', models.CharField(db_index=True, help_text='Use DDD, por exemplo 55987619832', max_length=11, unique=True, verbose_name='Número celular com DDD')),
                ('is_active', models.BooleanField(default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema', verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'ordering': ['-is_active', 'tipo', 'nome'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('administradores', usuario.models.AdministradorAtivoManager()),
                ('ordinarios', usuario.models.OrdinarioAtivoManager()),
            ],
        ),
    ]
