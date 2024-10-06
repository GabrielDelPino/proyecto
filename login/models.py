from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):  # Cambia a heredar de AbstractUser
    # Puedes agregar campos adicionales si lo necesitas
    pass


