from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_noticias, name='inicio'),
    path('noticias/', views.listar_noticias, name='listar_noticias'),
    path('articulos/', views.listar_articulos, name='listar_articulos'),
    path('cargar_noticia/', views.cargar_noticia, name='cargar_noticia'),
    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
]
