from django.contrib import admin
from .models import CustomUser  # Si tienes un modelo de usuario personalizado

# Register your models here.
admin.site.register(CustomUser)  # Registrar tu modelo de usuario personalizado si existe
