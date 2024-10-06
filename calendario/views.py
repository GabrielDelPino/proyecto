from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'calendario/calendar.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Asocia el evento al usuario actual
            event.save()
            return redirect('calendar')  # Redirige a la vista del calendario
    else:
        form = EventForm()
    return render(request, 'calendario/add_event.html', {'form': form})








