from django.db import models

# Create your models here.

#Clase Rol
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_rol
    

#Clase Usuario
class Usuario(models.Model):
    cedula = models.BigIntegerField(unique=True, null=True)
    nombre = models.CharField(max_length=100, null=True)
    primer_apellido = models.CharField(max_length=100, null=True)
    segundo_apellido = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    correo = models.EmailField(max_length=100, null=True)
    contrasena = models.CharField(max_length=100, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='rol')

    def __str__(self):
        return self.nombre
    
#Clase EstadoPago
class EstadoPago(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

#Clase TipoPago
class TipoPago(models.Model):
    descripcion = models.CharField(max_length=100, null=True)
    sigla = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.descripcion
    

#Clase OrdenPago
class OrdenesPago(models.Model):
    fecha_de_ingreso = models.DateField(auto_now_add=True)
    acreedor = models.CharField(max_length=100, null=True)
    factura = models.CharField(max_length=100, null=True, unique=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    moneda = models.CharField(max_length=100, null=True)
    id_estado_pago = models.ForeignKey(EstadoPago, on_delete=models.CASCADE, related_name='estado_pago')
    documentacion_compensacion = models.CharField(max_length=100,null=True)
    fecha_factura = models.DateField(null=True)
    fecha_pago = models.DateField(null=True)
    fecha_vencimiento = models.DateField(null=True)
    id_coordinador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='coordinador')
    id_tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, related_name='tipo_pago')
    urgente = models.CharField(max_length=100, null=True)
    id_analista = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='analista', null=True)
    fecha_revisado = models.DateField(null=True)

    def __str__(self):
        return f"Orden de pago {self.id} - {self.acreedor}"
    
#Clase TipoDevolucion
class TipoDevolucion(models.Model):
    descripcion = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.descripcion
    
#Clase Devoluciones
class Devoluciones(models.Model):
    descripcion = models.CharField(max_length=100, null=True)
    fecha_devolucion = models.DateField(auto_now_add=True) 
    cedula_usuario_devolucion = models.BigIntegerField(null=True)
    id_tipo_devolucion = models.ForeignKey(TipoDevolucion, on_delete=models.CASCADE, related_name='tipo_devolucion')
    id_orden_pago = models.ForeignKey(OrdenesPago, on_delete=models.CASCADE, related_name='orden_pago')
    id_analista = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='analista_devolucion')

    def __str__(self):
        return f"Devolucion {self.id} - {self.descripcion}"
    
#Clase Bitacora
class Bitacora(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    tabla = models.CharField(max_length=100, null=True)
    columna = models.CharField(max_length=100, null=True)
    valor_anterior = models.CharField(max_length=100, null=True)
    valor_despues = models.CharField(max_length=100, null=True)
    fecha_movimiento = models.DateField(auto_now_add=True)
    transaccion = models.CharField(max_length=100)
    fecha_movimiento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bitacora {self.id} - {self.tabla}"
