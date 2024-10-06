from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirigir a la vista de inicio de sesión
    path('home/', views.home, name='home'),  # Ruta para la página de inicio
    path('register/', views.register_view, name='register'),  # Ruta para la vista de registro
]














