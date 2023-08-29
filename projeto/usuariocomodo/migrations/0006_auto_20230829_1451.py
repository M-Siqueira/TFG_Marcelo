# Generated by Django 3.0.4 on 2023-08-29 17:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comodo', '0005_auto_20230829_1448'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuariocomodo', '0005_auto_20230829_1424'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usuariocomodo',
            unique_together={('usuario', 'comodo')},
        ),
        migrations.RemoveField(
            model_name='usuariocomodo',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='usuariocomodo',
            name='lugar',
        ),
    ]
