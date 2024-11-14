from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'usuarios-contraseña', views.UsuarioReadViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'roles', views.RolViewSet)
router.register(r'ordenes_pago', views.OrdenesPagoViewSet)
router.register(r'ordenes_pago_read', views.OrdenesPagoVer)
router.register(r'devoluciones', views.DevolucionesViewSet)
router.register(r'bitacora', views.BitacoraViewSet)
router.register(r'estados_pago', views.EstadoPagoViewSet)
router.register(r'tipos_pago', views.TipoPagoViewSet)
router.register(r'tipos_devolucion', views.TipoDevolucionViewSet)

app_name = 'api_pago'

urlpatterns = [
    #path('', include(router.urls)),
    path('', include(router.urls)),
]