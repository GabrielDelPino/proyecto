from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # Asegúrate de importar el formulario personalizado

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Iniciar sesión
                return redirect('calendar')  # Redirigir al calendario
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Usar el formulario personalizado
        if form.is_valid():
            form.save()  # Guardar el nuevo usuario
            return redirect('login')  # Redirigir al login después del registro
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'base.html')  # Asegúrate de que 'base.html' esté en el directorio correcto















