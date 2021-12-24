from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.conf import settings
from .models import Event, Booking
from .forms import ContactForm, BookingForm


class EventList(generic.ListView):
    #view to render the Event objects, max 9 per page
    model = Event

    Event.objects.all()
    template_name = 'events.html'


class HomePage(TemplateView):
    #view to render the homepage
    template_name = 'index.html'


def booking(request):
    #view to render the booking page
    booking_form = None
    # current_user = request.user
    # booking_form = BookingForm(initial={'user': current_user.username})
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            # booking_form.instance.user = request.user.username
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
    
    
class ManageBooking(generic.ListView):
    #view to render the manage booking page for logged in user
    model = Booking
    context_object_name = 'runs'
    paginate_by = 6
    template_name = 'manage.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    # def edit_booking()

def delete_booking(request, id):
    queryset = Booking.objects.filter(user=request.user)
    run = get_object_or_404(queryset, id=id)

    run.delete()

    return HttpResponseRedirect(reverse('manage'))

