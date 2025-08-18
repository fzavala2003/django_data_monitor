from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

"""
def home(request):
    return render(request, 'dashboard/base.html')
"""
@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON


    # Obtener la lista real de elementos dentro de "data"
    items = posts.get("data", {})

    # Contadores
    hotmail_count = 0
    month6_count = 0
    daniel_count = 0
    fechas=[]
    comentarios_length=[]

    for item in items.values():
        # Contar correos de hotmail
        if item.get("correo", "").lower().endswith("@hotmail.com"):
            hotmail_count += 1
        
        #fecha completa
        fecha = item.get("fecha", "")
        if fecha:
            fechas.append(fecha)

        # Contar fechas del mes 6
        fecha = item.get("fecha", "")
        if len(fecha) >= 7:  # formato ISO, ej: 2025-06-21...
            try:
                if fecha[5:7] == "06":
                    month6_count += 1
            except Exception:
                pass
        #longitud del comentario 
        comentario = item.get("comentario", "")
        if comentario:
            comentarios_length.append(len(comentario))


        # Contar nombres "daniel"
        if item.get("nombre", "").strip().lower() == "daniel":
            daniel_count += 1

    total_responses = len(items)

    filas = list(zip(fechas, comentarios_length))

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'hotmail_count': hotmail_count,
        'month6_count': month6_count,
        'daniel_count': daniel_count,
        "filas":filas,
        "registros_validos": len(fechas)
    }

    return render(request, 'dashboard/index.html', data)