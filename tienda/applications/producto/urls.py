from django.urls import path

from .views import ListProductUser, ListProductStok, ListProductGenero, FiltrarProductos

app_name = 'producto_app'

urlpatterns = [
    path('api/product/por-usuario/', ListProductUser.as_view(), name='product-producto_by_user'),
    path('api/product/con-stok/', ListProductStok.as_view(), name='producto_con_stok'),
    path('api/product/por-genero/<gender>', ListProductGenero.as_view(), name='producto_por_genero'),
    path('api/product/filtrar/', FiltrarProductos.as_view(), name='product-filtrar'),

]
