from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ObraForma
from .models import Obra
from datetime import datetime

def hello(request):
    fecha_hoy = datetime.now().strftime("%d de %B de %Y",)  
    return render(request, 'myapp/descripcion.html', {'fecha_hoy': fecha_hoy})  

def crear_obra(request):
    if request.method == 'POST':
        form = ObraForma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_obras')  
    else:
        form = ObraForma()  

    return render(request, 'myapp/crear_obra.html', {'form': form})
    


def mostrar_obras(request):
    obras = Obra.objects.all()
    return render(request, 'myapp/mostrar_obras.html', {'obras': obras})


