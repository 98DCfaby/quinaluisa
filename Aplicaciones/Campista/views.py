from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Campista

# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')
# ====================== Campista ======================
# Mostrar formulario para crear un nuevo campista
def nuevo_campista(request):
    return render(request, 'campista.html')  
# Mostrar formulario para listar campistas
def listar_campista(request):
    campistas=Campista.objects.all()
    return render(request, 'listadoCampista.html', {'campistas': campistas})

#===========================GUARDAR CAMPISTA=====================
def guardar_campista(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombres = request.POST.get('txt_nombre')
        correo = request.POST.get('txt_correo')
        telefono = request.POST.get('txt_telefono')
        direccion = request.POST.get('txt_direccion')

        # Validar que los campos obligatorios no estén vacíos
        if not nombres or not correo or not telefono:
            messages.error(request, "Por favor, completa todos los campos obligatorios.")
            return redirect('nuevo_campista')
        
        # Crear el nuevo campista y guardarlo en la base de datos
        Campista.objects.create(
            nombres=nombres,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )
        messages.success(request, "Campista agregado correctamente.")
        return redirect('listar_campista')
    else:
        # Si no es una solicitud POST, redirige a la página de nuevo campista
        return redirect('nuevo_campista')
