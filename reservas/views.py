from django.shortcuts import render, get_object_or_404, redirect
from .models import Campista
from .forms import CampistaForm
# Create your views here.


def index(request):
    return render(request, 'index.html')  
def campista_list(request):
    campistas = Campista.objects.all()
    return render(request, 'campista_list.html', {'campistas': campistas})

def campista_detail(request, id):
    campista = get_object_or_404(Campista, pk=id)
    return render(request, 'campista_detail.html', {'campista': campista})

def campista_create(request):
    if request.method == "POST":
        form = CampistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campista_list')
    else:
        form = CampistaForm()
    return render(request, 'campista_form.html', {'form': form})

def campista_edit(request, id):
    campista = get_object_or_404(Campista, pk=id)
    if request.method == "POST":
        form = CampistaForm(request.POST, instance=campista)
        if form.is_valid():
            form.save()
            return redirect('campista_list')
    else:
        form = CampistaForm(instance=campista)
    return render(request, 'campista_form.html', {'form': form})

def campista_delete(request, id):
    campista = get_object_or_404(Campista, pk=id)
    campista.delete()
    return redirect('campista_list')

from .models import Reserva
from .forms import ReservaForm

def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva_list.html', {'reservas': reservas})

def reserva_detail(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    return render(request, 'reserva_detail.html', {'reserva': reserva})

def reserva_create(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm()
    return render(request, 'reserva_form.html', {'form': form})

def reserva_edit(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva_form.html', {'form': form})

def reserva_delete(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    return redirect('reserva_list')