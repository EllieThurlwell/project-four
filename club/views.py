from django.shortcuts import render
from django.views import generic, View
from django.views.generic.base import TemplateView
from .models import Event

class EventList(generic.ListView):
    #view to render the Event objects, max 9 per page
    model = Event

    Event.objects.all()
    template_name = 'events.html'


class HomePage(TemplateView):
    
    template_name = 'index.html'
