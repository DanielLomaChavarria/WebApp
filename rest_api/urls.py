from django.urls import path
from . import views

urlpatterns = [
    path('videojuegos/', views.VideojuegoListCreateAPIView.as_view(), name='videojuego-list-create'),
    path('videojuegos/<int:pk>/', views.VideojuegoRetrieveUpdateDestroyAPIView.as_view(), name='videojuego-detail'),
    path('perfiles/', views.PerfilListCreateAPIView.as_view(), name='perfil-list-create'),
    path('perfiles/<int:pk>/', views.PerfilRetrieveUpdateDestroyAPIView.as_view(), name='perfil-detail'),
]
