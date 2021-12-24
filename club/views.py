from django.shortcuts import render, reverse
from django.views import generic, View
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.conf import settings
from .models import Event, Booking
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
            return HttpResponseRedirect(reverse('booking'))
    else:
        booking_form = BookingForm()

    context = {'booking_form': booking_form}

    return render(request, 'booking.html', context)
    model = Booking
    booked_run = Booking.objects.create(
        user=request.user,
        first_name=fname,
        last_name=lname,
        email=email,
        date=date
    )
    booked_run.save()

def contact(request):
    #view to render the Contact form to contact.html
    contact_form = None
    if request.method == 'POST':    
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            return HttpResponseRedirect(reverse('contact'))
    else:
        contact_form = ContactForm()

    context = {'contact_form': contact_form}

    return render(request, 'contact.html', context)
    
    
