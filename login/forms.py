from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Importa tu modelo personalizado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.',
            'password1': 'La contraseña no puede ser demasiado similar a otra información personal. Debe contener al menos 8 caracteres y no puede ser completamente numérica.',
            'password2': 'Introduce la misma contraseña que antes, para verificar.',
        }



