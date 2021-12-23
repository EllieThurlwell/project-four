from django.shortcuts import render, reverse
from django.views import generic, View
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.conf import settings
from .models import Event
from .forms import ContactForm, BookingForm
from bcnrun.settings import MAPS_API_KEY

class EventList(generic.ListView):
    #view to render the Event objects, max 9 per page
    model = Event

    Event.objects.all()
    template_name = 'events.html'


def getMap(request):
    #view to render the map to events page
    context = Context({"api_key": MAPS_API_KEY})
    # context = { 'api_key': settings.MAPS_API_KEY}
    return render(request,'events.html', context)


class HomePage(TemplateView):
    #view to render the homepage
    template_name = 'index.html'


def booking(request):
    #view to render the booking page
    booking_form = None
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form = booking_form.save()
    else:
        booking_form = BookingForm()
    return render(request, 'booking.html', {'booking_form': booking_form})


def contact(request):
    #view to render the Contact form to contact.html
    contact_form = None
    if request.method == 'POST':    
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
    return HttpResponseRedirect(reverse('home'))
    
