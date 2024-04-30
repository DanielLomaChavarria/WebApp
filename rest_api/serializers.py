from rest_framework import serializers
from core.models import Videojuego, Perfil
from django.contrib.auth.models import User

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['id', 'tipo_videojuego', 'comentario', 'puntuacion', 'fecha_registro', 'usuario']

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'usuario', 'nombre', 'apellido', 'numero', 'correo', 'genero', 'direccion']
