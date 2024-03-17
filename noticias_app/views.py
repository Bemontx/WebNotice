from django.conf import settings
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Noticia, Articulo, Comentario
from .forms import NoticiaForm, ComentarioForm
import os


def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias_app/listar_noticias.html', {'noticias': noticias})

def listar_articulos(request):
    articulos = Articulo.objects.all()
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return render(request, 'noticias_app/listar_noticias.html', {'articulos': articulos, 'fecha_actual': fecha_actual})

def cargar_noticia(request):
    BASE_DIR = settings.BASE_DIR
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias_app/listar_noticias.html', {'form': form})


def guardar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('listar_noticias')
        else:
            print(form.errors)
    else:
        form = ComentarioForm()  
    return render(request, 'noticias_app/listar_noticias.html', {'form': form})
