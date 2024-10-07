from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),  # Vista del calendario
    path('add/', views.event_create, name='event_create'),  # Vista para crear un evento
    path('load_events/', views.load_events, name='load_events'),  # Vista para cargar eventos en el calendario
]







