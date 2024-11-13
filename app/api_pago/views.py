
from rest_framework import viewsets, mixins, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

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