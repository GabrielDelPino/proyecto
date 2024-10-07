from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Asociar el evento al usuario actual
            event.save()
            return redirect('calendar')  # Redirige al calendario tras guardar
    else:
        form = EventForm()
    return render(request, 'calendario/add_event.html', {'form': form})

@login_required
def load_events(request):
    events = Event.objects.filter(user=request.user)
    events_json = [
        {
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
            'description': event.description
        }
        for event in events
    ]
    return JsonResponse(events_json, safe=False)

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'calendario/calendar.html', {'events': events})











