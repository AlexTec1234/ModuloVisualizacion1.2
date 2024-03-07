from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DashboardValor
from .serializers import DashboardValorSerializer

class ConsultarDatosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener parámetros de la consulta
        nombre_campo = request.query_params.get('nombre_campo', '')
        cantidad_valores = int(request.query_params.get('cantidad_valores', 0))

        try:
            # Consultar la base de datos para obtener los datos
            queryset = DashboardValor.objects.filter(campo__nombre_de_campo=nombre_campo).order_by('-id')[:cantidad_valores]
            serializer = DashboardValorSerializer(queryset, many=True)

            # Procesar los datos y prepararlos para la respuesta
            resultados_json = []
            for row in serializer.data:
                valor_decimal = round(float(row['valor']) / 10, 2) if nombre_campo.lower() == 'humedad' else round(float(row['valor']), 2)
                if valor_decimal >= 0:
                    resultados_json.append({"ID": row['id'], "Valor": valor_decimal})

            # Devolver los datos en formato JSON
            return Response({"datos": resultados_json}, status=status.HTTP_200_OK)

        except Exception as e:
            # Manejar errores y devolver una respuesta de error adecuada
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
