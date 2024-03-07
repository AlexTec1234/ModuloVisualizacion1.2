import requests
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.embed import components
from django.shortcuts import render
#-----------------------------------
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from django.shortcuts import render
import base64
from io import BytesIO  # Agregar esta línea
from django.template import loader

# Create your views here.
def inicio(request):
    template=loader.get_template('prindex.html')
    #llama y retorna al html para devolver la vitsa
    return HttpResponse(template.render())
def sensores(request):
    template=loader.get_template('sensores.html')
    #llama y retorna al html para devolver la vitsa
    return HttpResponse(template.render())
def menu(request):
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, 'menu.html', {})

#def plotye(request):
    #template=loader.get_template('ploty.html')
    #llama y retorna al html para devolver la vitsa
    #return HttpResponse(template.render())

#creacion de grafica con matplolib

def graficas(request):
    if request.method == 'POST':
        nombre_campo = request.POST.get('nombre_campo', '')
        cantidad_valores = request.POST.get('cantidad_valores', '')

        # Realizar la solicitud a la API para obtener los datos
        api_url = 'http://localhost:8000/api/consultar-datos/'
        params = {'nombre_campo': nombre_campo, 'cantidad_valores': cantidad_valores}
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()

            campo_label = nombre_campo.capitalize()  # Convertir el nombre del campo a mayúscula para mostrarlo correctamente

            x = [item['ID'] for item in data['datos']]

            # Crear la figura y los ejes
            fig, ax = plt.subplots()

            # Obtener los datos del campo 'Valor'
            campo_data = [item['Valor'] for item in data['datos']]

            ax.plot(x, campo_data)
            ax.set_xlabel('ID')
            ax.set_ylabel(campo_label)
            ax.set_title('Gráfico de {}'.format(campo_label))

            # Convertir la figura a una imagen PNG en memoria
            buffer = BytesIO()
            canvas = FigureCanvasAgg(fig)
            canvas.print_png(buffer)
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            # Convertir la imagen a base64
            graph_image = base64.b64encode(image_png).decode()

            return render(request, 'graficas.html', {'graph_image': graph_image, 'campo_label': campo_label})
        else:
            return render(request, 'graficas.html', {'error': 'Error al obtener los datos de la API'})
    else:
        return render(request, 'graficas.html')


#bokeh
def bokeh(request):
    if request.method == 'POST':
        nombre_campo = request.POST.get('nombre_campo', '')
        cantidad_valores = request.POST.get('cantidad_valores', '')

        if nombre_campo and cantidad_valores:
            try:
                api_url = 'http://localhost:8000/api/consultar-datos/'
                params = {'nombre_campo': nombre_campo, 'cantidad_valores': cantidad_valores}
                response = requests.get(api_url, params=params)

                if response.status_code == 200:
                    data = response.json()
                    x_values = [item['ID'] for item in data['datos']]
                    y_values = [item['Valor'] for item in data['datos']]
                    return render(request, 'bokeh.html', {'x_values': x_values, 'y_values': y_values, 'error': None})
                else:
                    return render(request, 'bokeh.html', {'x_values': None, 'y_values': None, 'error': 'Error al obtener los datos de la API'})
            except Exception as e:
                return render(request, 'bokeh.html', {'x_values': None, 'y_values': None, 'error': str(e)})
        else:
            return render(request, 'bokeh.html', {'x_values': None, 'y_values': None, 'error': 'Por favor, proporcione el nombre del campo y la cantidad de valores'})
    else:
        return render(request, 'bokeh.html', {'x_values': None, 'y_values': None, 'error': None})



#aqui se regresan los datos a ploty.html
def plotye(request):
    if request.method == 'POST':
        nombre_campo = request.POST.get('nombre_campo', '')
        cantidad_valores = request.POST.get('cantidad_valores', '')

        # Realizar la solicitud a la API para obtener los datos
        api_url = 'http://localhost:8000/api/consultar-datos/'
        params = {'nombre_campo': nombre_campo, 'cantidad_valores': cantidad_valores}
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()

            campo_label = nombre_campo.capitalize()  # Convertir el nombre del campo a mayúscula para mostrarlo correctamente

            # Imprime los datos en la consola del servidor Django
            print(data)

            # Pasa los datos obtenidos de la API como contexto a la plantilla ploty.html
            return render(request, 'ploty.html', {'data': data, 'selected_field': campo_label})
        else:
            return render(request, 'ploty.html', {'error': 'Error al obtener los datos de la API'})
    else:
        return render(request, 'ploty.html')

