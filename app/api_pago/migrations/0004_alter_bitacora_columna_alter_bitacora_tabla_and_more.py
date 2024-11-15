# Generated by Django 4.2.5 on 2024-11-15 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_pago', '0003_alter_usuario_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='columna',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='tabla',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='valor_anterior',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='valor_despues',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devoluciones',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='acreedor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='descuento',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='documentacion_compensacion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='factura',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='fecha_factura',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='fecha_pago',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='fecha_revisado',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='fecha_vencimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='id_analista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analista', to='api_pago.usuario'),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='impuesto',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='moneda',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='urgente',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tipodevolucion',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tipodevolucion',
            name='estado',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tipopago',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tipopago',
            name='sigla',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='primer_apellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundo_apellido',
            field=models.CharField(max_length=100, null=True),
        ),
    ]