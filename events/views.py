from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from django.http import Http404
from events.models import Event
from events.models import Calendar


def index(request):
    calendars = Calendar.objects.all()
    return render_to_response(
        'events/index.html',
        {'calendars': calendars},
        context_instance=RequestContext(request)
    )


def calendar_events(request, calendar_slug=None):
    events = Event.objects.filter(calendar__slug=calendar_slug).filter(end__gte=datetime.date.today()).order_by('start')
    calendars = Calendar.objects.all()
    calendar = calendars.get(slug=calendar_slug)
    if not calendar:
        raise Http404
    return render_to_response(
        'events/calendar_events.html',
        {'events': events, 'calendar': calendar, 'calendars': calendars},
        context_instance=RequestContext(request)
    )


def event_detail(request, calendar_slug=None, event_slug=None):
    calendars = Calendar.objects.all()
    try:
        event = Event.objects.get(slug=event_slug)
    except Event.DoesNotExist:
        raise Http404
    return render_to_response(
        'events/event_detail.html',
        {'event': event, 'calendars': calendars},
        context_instance=RequestContext(request)
    )
