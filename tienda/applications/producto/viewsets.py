from rest_framework.response import Response
from rest_framework import viewsets
from .models import Colors, Product
from .serializers import (
    ColorSerializer,
    ProductSerializer,
    PaginationSerializer,
    ProductSerializerViewSet,
)

# CRUD: Create, Read, Update, Delete
class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Colors.objects.all()


# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#     pagination_class = PaginationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer

    def perform_create(self, serializer):
        # antes de guardar los datos, el atributo video recibe el siguiente link:
        serializer.save(
            video = "https://www.youtube.com/watch?v=aEoNw3uiTY0&list=RDaEoNw3uiTY0"
        )

    # def list(self, request, *args, **kwargs):
    #     queryset = Product.objects.productos_por_user(self.request.user)
    #     serializer = self.get_serializer(queryset, many = True)
    #     return Response(serializer.data)