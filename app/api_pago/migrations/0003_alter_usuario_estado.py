# Generated by Django 4.2.5 on 2024-11-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_pago', '0002_alter_usuario_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(max_length=100),
        ),
    ]
