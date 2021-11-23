from django.contrib import admin
from django.urls import path, include
from passagens.views import VooViewSet, StatusViewSet, ClientesViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Passagens",
      default_version='v1.0',
      description="Api com cadastro simples de clientes, voos e status do pagamento dos clientes",
      terms_of_service="#",
      contact=openapi.Contact(email="https://github.com/rhama-krisner"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('voo', VooViewSet, basename='Voo')
router.register('status', StatusViewSet, basename='Status')
router.register('clientes', ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
