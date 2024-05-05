from django.urls import path
from .views import index, videojuegos, registrate, sesion, vermas, foro, registrate, sesion
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('videojuegos/', videojuegos, name="videojuegos"),
    path('vermas/', vermas, name="vermas"),
    path('foro/', foro, name="foro"),
    path('registrate/', registrate, name="registrate"),
    path('sesion/', sesion, name='sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='logout'),
    path('crear-videojuego/', views.crear_videojuego, name='crear_videojuego'),
    path('ver-perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('crear-perfil/', views.crear_perfil, name='crear_perfil'),
    path('borrar-comentario/<int:comentario_id>/', views.borrar_comentario, name='borrar_comentario'),
    path('actualizar-comentario/<int:comentario_id>/', views.actualizar_comentario, name='actualizar_comentario'),

    

]   
