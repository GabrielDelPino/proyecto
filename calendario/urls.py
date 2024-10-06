from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),  # Vista del calendario
    path('add/', views.event_create, name='event_create'),  # Vista para crear un evento
]






