from rest_framework import serializers
from .models import Sale, SaleDetail


class VentaReporteSerializer(serializers.ModelSerializer):
    """ serializador para ver las ventas en detalle """

    productos = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',
            'productos',
        )

    def get_productos(self, obj):
        query = SaleDetail.objects.productos_por_venta(obj.id)
        productos_serializados = DetalleVentaProductoSerializer(
            query, many=True).data
        return productos_serializados


class DetalleVentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale',
        )


class ProductDetailSerializers(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()


class ProcesoVentaSerializer(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ProductDetailSerializers(many=True)


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class ProcesoVentaSerializer2(serializers.Serializer):
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ArrayIntegerSerializer()
    cantidades = ArrayIntegerSerializer()

    # si el tipo de pago es diferente de 0 no se puede realizar la venta
    def validate(self, data):
        if data['type_payment'] != '0':
            raise serializers.ValidationError('Ingrese un tipo de pago correcto')
        return data

    # si el tipo de factura es diferente de 0 no se puede realizar la venta
    def validate_type_invoce(self, value):
        if value != '0':
            raise serializers.ValidationError('Ingrese un valor correcto')
        return value