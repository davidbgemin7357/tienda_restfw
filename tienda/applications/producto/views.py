from unicodedata import name
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    # ! ESTO ES LO QUE PROTEGE LAS RUTAS (CON TOKEN SOLICITADO)
    permission_classes = [IsAuthenticated]
    # solo permitirá el acceso a la vista si el usuario logueado es admin
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        # recuperando usuario:
        usuario = self.request.user
        return Product.objects.productos_por_user(usuario)


class ListProductStok(ListAPIView):
    serializer_class = ProductSerializer
    # authentication_classes: solo verifica si es usuario o no es usuario (incluye al AnonymousUser) por lo cual la vista se muestra sin restricción
    authentication_classes = (TokenAuthentication,)
    # permission_classes: te pide necesariamente que se envíe un token por lo cual hay una restricción:
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # recuperando usuario:
        usuario = self.request.user
        return Product.objects.productos_con_stok()


class ListProductGenero(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        genero = self.kwargs['gender']
        return Product.objects.productos_por_genero(genero)


class FiltrarProductos(ListAPIView):
    """"""
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        varon = self.request.query_params.get('man', None)
        mujer = self.request.query_params.get('woman', None)
        nombre = self.request.query_params.get('name', None)
        
        return Product.objects.filtrar_productos(
            man=varon,
            woman=mujer,
            name=nombre
        )