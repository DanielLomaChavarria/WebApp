
from rest_framework import generics

from rest_framework.response import Response
#Visualizaciòn del API Rest
from rest_framework.decorators import api_view
# Seguridad (Eliminar o activar)
from django.views.decorators.csrf import csrf_exempt
# Formato Json
from rest_framework.parsers import JSONParser
#libreria de còdigo de respuesta
from rest_framework import status

from core.models import Videojuego
from .serializers import VideojuegoSerializer
from core.models import Perfil
from .serializers import PerfilSerializer


# Vistas para Videojuegos
class VideojuegoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer

    def get(self, request, *args, **kwargs):
        # Lógica para obtener una lista de todos los videojuegos
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Lógica para crear un nuevo videojuego
        return self.create(request, *args, **kwargs)

class VideojuegoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer
    lookup_field = 'pk'  # Campo de búsqueda para recuperar, actualizar y eliminar un videojuego específico

    def get(self, request, *args, **kwargs):
        # Lógica para obtener un videojuego específico por su ID
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Lógica para actualizar un videojuego específico por su ID
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Lógica para actualizar parcialmente un videojuego específico por su ID
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Lógica para eliminar un videojuego específico por su ID
        return self.destroy(request, *args, **kwargs)

# Vistas para Perfiles
class PerfilListCreateAPIView(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    def get(self, request, *args, **kwargs):
        # Lógica para obtener una lista de todos los perfiles
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Lógica para crear un nuevo perfil
        return self.create(request, *args, **kwargs)

class PerfilRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    lookup_field = 'pk'  # Campo de búsqueda para recuperar, actualizar y eliminar un perfil específico

    def get(self, request, *args, **kwargs):
        # Lógica para obtener un perfil específico por su ID
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Lógica para actualizar un perfil específico por su ID
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Lógica para actualizar parcialmente un perfil específico por su ID
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Lógica para eliminar un perfil específico por su ID
        return self.destroy(request, *args, **kwargs)



