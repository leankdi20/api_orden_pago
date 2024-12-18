from rest_framework import serializers
from .models import Rol, Usuario, EstadoPago, TipoPago, OrdenesPago, TipoDevolucion, Devoluciones, Bitacora


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre_rol'] 


class UsuarioSerializer(serializers.ModelSerializer):
    # id_rol = RolSerializer(many=False)

    class Meta:
        model = Usuario
        fields = '__all__'

class EstadoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPago
        fields = ['id', 'descripcion']

class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = ['id', 'descripcion', 'sigla']

class OrdenesPagoSerializer(serializers.ModelSerializer):
    # id_estado_pago = EstadoPagoSerializer(many=False, required=True)
    # id_coordinarod = UsuarioSerializer(many=False, required=True)
    # id_tipo_pago = TipoPagoSerializer(many=False, required=True)
    # id_analista = UsuarioSerializer(many=False, required=True)

    class Meta:
        model = OrdenesPago
        fields = '__all__'

class OrdenesPagoReadSerializer(serializers.ModelSerializer):
    id_estado_pago = EstadoPagoSerializer(many=False, required=True)
    id_coordinador = UsuarioSerializer(many=False, required=True)
    id_tipo_pago = TipoPagoSerializer(many=False, required=True)
    id_analista = UsuarioSerializer(many=False, required=True)

    class Meta:
        model = OrdenesPago
        fields = '__all__'

class OrdenesPagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdenesPago
        fields = '__all__'


class TipoDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDevolucion
        fields = '__all__'

class DevolucionesSerializer(serializers.ModelSerializer):
    # id_tipo_devolucion = TipoDevolucionSerializer(many=False, required=True)
    # id_orden_pago = OrdenesPagoSerializer(many=False, required=True)
    # id_analista = UsuarioSerializer(many=False, required=True)

    class Meta:
        model = Devoluciones
        fields = '__all__'

class BitacoraSerializer(serializers.ModelSerializer):
    # id_usuario = UsuarioSerializer(many=False, required=True)
    
    class Meta:
        model = Bitacora
        fields = '__all__'




#Vista por un usuario
class UsuarioCredencialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'