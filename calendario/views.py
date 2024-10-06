from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'calendario/calendar.html', {'events': events})





