from django.urls import path
from .views import ConsultarDatosAPIView
 
urlpatterns = [
    path('consultar-datos/', ConsultarDatosAPIView.as_view(), name='consultar-datos-api'),
]