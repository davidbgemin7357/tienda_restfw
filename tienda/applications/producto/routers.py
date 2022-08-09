from rest_framework.routers import DefaultRouter
from .viewsets import ColorViewSet, ProductViewSet

router = DefaultRouter()

router.register(r'colors', ColorViewSet, basename='colors')
router.register(r'productos', ProductViewSet, basename='productos')

urlpatterns = router.urls