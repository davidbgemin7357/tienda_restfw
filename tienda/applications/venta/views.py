from django.utils import timezone
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from applications.producto.models import Product
from .serializers import (
    VentaReporteSerializer,
    ProcesoVentaSerializer,
    ProcesoVentaSerializer2,
)

from rest_framework.response import Response

from .models import Sale, SaleDetail, Product
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ReporteVentasList(ListAPIView):
    serializer_class = VentaReporteSerializer

    def get_queryset(self):
        return Sale.objects.all()

# -------Vista para registrar una nueva venta-------
class RegistrarVenta(CreateAPIView):
    """registra una venta"""
    authentication_classes =  (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args):
        serializer = ProcesoVentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tipo_recibo = serializer.validated_data['type_invoce']

        # atributo del tipo colección:
        venta = Sale.objects.create(
            date_sale = timezone.now(),
            amount = 0,
            count = 0,
            type_invoce = serializer.validated_data['type_invoce'],
            type_payment = serializer.validated_data['type_payment'],
            adreese_send = serializer.validated_data['adreese_send'],   
            user = self.request.user,
        )
        # variables para venta
        amount = 0
        count = 0

        # recuperamos los productos de la venta (producto no es parte del modelo):
        productos = serializer.validated_data['productos']

        # 
        ventas_detalle = []
        for producto in productos:
            # pk es viene del serializer ProductDetailSerializers
            prod = Product.objects.get(id=producto['pk'])
            venta_detalle = SaleDetail(
                sale = venta,
                product = prod,
                count = producto['count'],
                price_purchase = prod.price_purchase,
                price_sale = prod.price_sale,
            )
            amount = amount + prod.price_sale * producto['count']
            count = count + producto['count']
            ventas_detalle.append(venta_detalle)

        venta.amount = amount
        venta.count = count
        venta.save()
        SaleDetail.objects.bulk_create(ventas_detalle)

        # respuesta Json:
        return Response({"msg": "Venta registrada correctamente"})



class RegistrarVenta2(CreateAPIView):
    """registra una venta"""
    authentication_classes =  (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = ProcesoVentaSerializer2

    def create(self, request, *args):
        serializer = ProcesoVentaSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)

        tipo_recibo = serializer.validated_data['type_invoce']

        # atributo del tipo colección:
        venta = Sale.objects.create(
            date_sale = timezone.now(),
            amount = 0,
            count = 0,
            type_invoce = serializer.validated_data['type_invoce'],
            type_payment = serializer.validated_data['type_payment'],
            adreese_send = serializer.validated_data['adreese_send'],   
            user = self.request.user,
        )
        # variables para venta
        amount = 0
        count = 0

        # recuperamos los productos de la venta (producto no es parte del modelo):
        productos = Product.objects.filter(
            id__in=serializer.validated_data['productos']
        )
        cantidades = serializer.validated_data['cantidades']

        # 
        ventas_detalle = []
        for producto, cantidad in zip(productos, cantidades):
            venta_detalle = SaleDetail(
                sale = venta,
                product = producto,
                count = cantidad,
                price_purchase = producto.price_purchase,
                price_sale = producto.price_sale,
            )
            amount = amount + producto.price_sale * cantidad
            count = count + cantidad
            ventas_detalle.append(venta_detalle)

        venta.amount = amount
        venta.count = count
        venta.save()
        SaleDetail.objects.bulk_create(ventas_detalle)

        # respuesta Json:
        return Response({"msg": "Venta registrada correctamente"})