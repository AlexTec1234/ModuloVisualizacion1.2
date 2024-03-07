from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('sensores/',views.sensores, name='sensores'),
    path('menu/', views.menu, name='menu'),
    path('graficas/', views.graficas, name='graficas'),
    path('bokeh/', views.bokeh, name='bokeh'),
    path('GraficaP/', views.plotye, name='GraficaP'),
    ]