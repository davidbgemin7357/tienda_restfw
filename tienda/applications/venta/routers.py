from rest_framework.routers import DefaultRouter

from .viewsets import VentasViewSet

router = DefaultRouter()

router.register(r'ventas', VentasViewSet, basename='ventas')

urlpatterns = router.urls