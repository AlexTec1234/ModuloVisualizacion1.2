# serializers.py
from rest_framework import serializers
from .models import DashboardCampo, DashboardDispositivo, DashboardProyecto, DashboardSensor, DashboardValor

class DashboardCampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardCampo
        fields = ['nombre_de_campo', 'tipo_de_valor']

class DashboardDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardDispositivo
        fields = ['nombre_de_dispositivo', 'descripcion', 'tipo']

class DashboardProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardProyecto
        fields = ['nombre_de_proyecto', 'descripcion']

class DashboardSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardSensor
        fields = ['nombre_de_sensor', 'tipo']

class DashboardValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardValor
        fields = ['id', 'valor', 'fecha_hora_lectura', 'campo']
