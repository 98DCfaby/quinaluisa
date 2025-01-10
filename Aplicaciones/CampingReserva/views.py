from django.shortcuts import render, get_object_or_404, redirect
from .models import Campista, Reserva
from .forms import CampistaForm, ReservaForm

def home(request):
    return redirect('lista_campistas')

# CRUD Campistas
def lista_campistas(request):
    campistas = Campista.objects.all()
    return render(request, 'lista_campistas.html', {'campistas': campistas})

def detalle_campista(request, pk):
    campista = get_object_or_404(Campista, pk=pk)
    return render(request, 'detalle_campista.html', {'campista': campista})

def crear_campista(request):
    if request.method == 'POST':
        form = CampistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campistas')
    else:
        form = CampistaForm()
    return render(request, 'formulario_campista.html', {'form': form})

def editar_campista(request, pk):
    campista = get_object_or_404(Campista, pk=pk)
    if request.method == 'POST':
        form = CampistaForm(request.POST, instance=campista)
        if form.is_valid():
            form.save()
            return redirect('lista_campistas')
    else:
        form = CampistaForm(instance=campista)
    return render(request, 'formulario_campista.html', {'form': form})

def eliminar_campista(request, pk):
    campista = get_object_or_404(Campista, pk=pk)
    campista.delete()
    return redirect('lista_campistas')

# CRUD Reservas
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reservas.html', {'reservas': reservas})

def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'formulario_reserva.html', {'form': form})

def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'formulario_reserva.html', {'form': form})

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('lista_reservas')
