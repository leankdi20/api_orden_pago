
from rest_framework import viewsets, mixins, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse

from .models import Usuario, Rol, OrdenesPago, Devoluciones, Bitacora, EstadoPago, TipoPago, TipoDevolucion
from .serializers import (
    UsuarioSerializer,
    RolSerializer,
    OrdenesPagoSerializer,
    DevolucionesSerializer,
    BitacoraSerializer,
    EstadoPagoSerializer,
    TipoPagoSerializer,
    TipoDevolucionSerializer,
    OrdenesPagoReadSerializer,
    UsuarioCredencialesSerializer
)

from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
def test_error(request):
    # Esta línea genera un error deliberado
    raise Exception("Este es un error de prueba para enviar a Slack.")
    return HttpResponse("Todo está bien.")


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset

class OrdenesPagoViewSet(viewsets.ModelViewSet):
    queryset = OrdenesPago.objects.all()
    serializer_class = OrdenesPagoSerializer
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.queryset
        # Filtros específicos
        id_estado = self.request.GET.get('id_estado', None)
        id_tipo_de_pago = self.request.GET.get('id_tipo_de_pago', None)
        fecha_vencimiento = self.request.GET.get('fecha_vencimiento', None)
        
        if id_estado:
            query = query.filter(id_estado=id_estado)
        if id_tipo_de_pago:
            query = query.filter(id_tipo_de_pago=id_tipo_de_pago)
        if fecha_vencimiento:
            query = query.filter(fecha_vencimiento__lte=fecha_vencimiento)

        return query
    
    @action(detail=True, methods=['patch'])
    def actualizar_estado_pago(self, request, pk=None):
        orden_pago = self.get_object()  # Obtén el objeto OrdenPago con el pk de la URL

        # Extrae el nuevo estado de pago de la solicitud
        id_estado_pago = request.data.get('id_estado_pago')

        if id_estado_pago:
            try:
                estado_pago = EstadoPago.objects.get(id=id_estado_pago)
                orden_pago.id_estado_pago = estado_pago
                orden_pago.save()  
                return Response({"message": "Estado de pago actualizado"}, status=status.HTTP_200_OK)
            except EstadoPago.DoesNotExist:
                return Response({"error": "Estado de pago no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "id_estado_pago no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
    
    def registrar_bitacora(self, objeto, campo_modificado, valor_anterior, valor_nuevo, transaccion,id_usuario):
        """
        Registra el cambio de un objeto en la bitácora.
        """
        bitacora = Bitacora(
            id_usuario=id_usuario, 
            tabla=objeto.__class__.__name__, 
            columna=campo_modificado,  
            valor_anterior=valor_anterior, 
            valor_despues=valor_nuevo,  
            transaccion=transaccion, 
            fecha_movimiento=timezone.now()  
        )
        bitacora.save()


class OrdenesPagoVer(mixins.RetrieveModelMixin, mixins.ListModelMixin , viewsets.GenericViewSet):
    queryset = OrdenesPago.objects.all()
    serializer_class = OrdenesPagoReadSerializer
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.queryset
        # Filtros específicos
        id_estado = self.request.GET.get('id_estado', None)
        id_tipo_de_pago = self.request.GET.get('id_tipo_de_pago', None)
        fecha_vencimiento = self.request.GET.get('fecha_vencimiento', None)
        
        if id_estado:
            query = query.filter(id_estado=id_estado)
        if id_tipo_de_pago:
            query = query.filter(id_tipo_de_pago=id_tipo_de_pago)
        if fecha_vencimiento:
            query = query.filter(fecha_vencimiento__lte=fecha_vencimiento)

        return query


class DevolucionesViewSet(viewsets.ModelViewSet):
    queryset = Devoluciones.objects.all()
    serializer_class = DevolucionesSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        id_tipo_devolucion = self.request.GET.get('id_tipo_devolucion', None)
        id_orden_de_pago = self.request.GET.get('id_orden_de_pago', None)
        
        if id_tipo_devolucion:
            queryset = queryset.filter(id_tipo_devolucion=id_tipo_devolucion)
        if id_orden_de_pago:
            queryset = queryset.filter(id_orden_de_pago=id_orden_de_pago)

        return queryset


class BitacoraViewSet(viewsets.ModelViewSet):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class EstadoPagoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPago.objects.all()
    serializer_class = EstadoPagoSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class TipoPagoViewSet(viewsets.ModelViewSet):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class TipoDevolucionViewSet(viewsets.ModelViewSet):
    queryset = TipoDevolucion.objects.all()
    serializer_class = TipoDevolucionSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]



#Vista de un usuario 
class UsuarioReadViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        correo = self.request.query_params.get('correo')
        if correo:
            return Usuario.objects.filter(correo=correo)
        return super().get_queryset()

    @action(detail=False, methods=['get'], url_path='credenciales')
    def credenciales(self, request):
        correo = request.query_params.get('correo')
        if correo:
            try:
                usuario = Usuario.objects.get(correo=correo)
                serializer = UsuarioCredencialesSerializer(usuario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Correo no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)