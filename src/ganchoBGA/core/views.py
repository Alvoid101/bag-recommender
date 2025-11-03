from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Bolso
from .forms import BolsoForm
import json

# Create your views here.

def home(request):
    """Vista principal con el carrusel de bolsos"""
    bolsos = Bolso.objects.all()[:10]  # Obtener los primeros 10 bolsos
    
    # Preparar datos para JavaScript
    bolsos_data = []
    for bolso in bolsos:
        bolsos_data.append({
            'id': bolso.id,
            'name': bolso.product_display_name,
            'color': bolso.base_colour,
            'image': bolso.image if bolso.image else '',
            'price': '58000'  # Precio por defecto, puedes ajustarlo según tu modelo
        })
    
    context = {
        'bolsos': bolsos,
        'bolsos_json': json.dumps(bolsos_data)
    }
    return render(request, 'core/home.html', context)


def colecciones(request):
    """Vista para mostrar todas las colecciones de bolsos"""
    bolsos = Bolso.objects.all()
    
    # Obtener colores únicos y ordenarlos
    colores = Bolso.objects.values_list('base_colour', flat=True).distinct().order_by('base_colour')
    
    # Filtrar por color si se proporciona
    color_filter = request.GET.get('color')
    if color_filter:
        bolsos = bolsos.filter(base_colour=color_filter)
    
    context = {
        'bolsos': bolsos,
        'colores': sorted(set(colores)),  # Asegurar que sean únicos y ordenados
        'color_seleccionado': color_filter
    }
    return render(request, 'core/colecciones.html', context)


def contacto(request):
    """Vista de contacto"""
    return render(request, 'core/contacto.html')


def agregar_bolso(request):
    """Vista para agregar un nuevo bolso"""
    if request.method == 'POST':
        form = BolsoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Bolso agregado exitosamente!')
            return redirect('colecciones')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = BolsoForm()
    
    return render(request, 'core/agregar_bolso.html', {'form': form})


def editar_bolso(request, bolso_id):
    """Vista para editar un bolso existente"""
    bolso = get_object_or_404(Bolso, id=bolso_id)
    
    if request.method == 'POST':
        form = BolsoForm(request.POST, request.FILES, instance=bolso)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Bolso actualizado exitosamente!')
            return redirect('colecciones')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = BolsoForm(instance=bolso)
    
    return render(request, 'core/editar_bolso.html', {'form': form, 'bolso': bolso})


def eliminar_bolso(request, bolso_id):
    """Vista para eliminar un bolso"""
    bolso = get_object_or_404(Bolso, id=bolso_id)
    
    if request.method == 'POST':
        bolso.delete()
        messages.success(request, '¡Bolso eliminado exitosamente!')
        return redirect('colecciones')
    
    return render(request, 'core/eliminar_bolso.html', {'bolso': bolso})
