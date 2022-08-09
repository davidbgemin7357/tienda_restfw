from django.urls import path

from .views import ReporteVentasList, RegistrarVenta, RegistrarVenta2

app_name = 'venta_app'

urlpatterns = [
    path('api/venta/reporte/', ReporteVentasList.as_view(), name='venta-reporte'),
    path('api/venta/create/', RegistrarVenta.as_view(), name='venta-register'),
    path('api/venta/add/', RegistrarVenta2.as_view(), name='venta-add'),
]
