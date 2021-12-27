from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from .models import Event, Booking, DAYS, LEVELS
from .forms import ContactForm, BookingForm


class HomePage(TemplateView):
    # view to render the homepage
    template_name = 'index.html'


# get string values from tuples
def get_day_from_dayint(dayint):
    for day_tuple in DAYS:
        if day_tuple[0] == dayint:
            return day_tuple[1]


def get_level_from_levelint(levelint):
    for level_tuple in LEVELS:
        if level_tuple[0] == levelint:
            return level_tuple[1]


class EventList(generic.ListView):
    # view to render the Event objects
    model = Event
    template_name = 'events.html'

    def get_queryset(self):
        events = Event.objects.all()
        for event in events:
            event.day_string = get_day_from_dayint(event.day)
            event.level_string = get_level_from_levelint(event.level)

        return events


def contact(request):
    # view to render the Contact form to contact.html
    contact_form = None
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 'Message sent!')
            return HttpResponseRedirect(reverse('contact'))
    else:
        contact_form = ContactForm()

    context = {'contact_form': contact_form}

    return render(request, 'contact.html', context)


def booking(request):
    # view to render the Booking form to booking.html
    booking_form = None

    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booked_run = Booking.objects.create(
                user=request.user,
                name=request.POST.get("name", ""),
                email=request.POST.get("email", ""),
                date=request.POST.get("date", "")
            )
            booked_run.save()
            messages.add_message(request, messages.SUCCESS, 'Run booked!')
            return HttpResponseRedirect(reverse('booking'))
    else:
        booking_form = BookingForm()

    context = {'booking_form': booking_form}

    return render(request, 'booking.html', context)


class ManageBooking(generic.ListView):
    # view to render the manage booking page for logged in user
    model = Booking
    context_object_name = 'runs'
    template_name = 'manage.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class EditBooking(View):
    # view to render the edit booking form for logged in user
    def get(self, request, id):
        queryset = Booking.objects.filter(user=request.user)
        run = get_object_or_404(queryset, id=id)
        context = {'edit_booking_form': BookingForm(instance=run)}
        return render(request, 'edit-booking.html', context)

    def post(self, request, id):
        queryset = Booking.objects.filter(user=request.user)
        run = get_object_or_404(queryset, id=id)
        edit_booking_form = BookingForm(request.POST, instance=run)
        context = {'edit_booking_form': BookingForm(instance=run)}

        if edit_booking_form.is_valid():
            edit_booking_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Booking successfully edited')
            return HttpResponseRedirect(reverse('manage'))

        return render(request, 'edit-booking.html', context)


def delete_booking(request, id):
    # view to delete a specific booking for logged in user
    queryset = Booking.objects.filter(user=request.user)
    run = get_object_or_404(queryset, id=id)

    run.delete()
    messages.add_message(request, messages.SUCCESS, 'Booking cancelled')
    return HttpResponseRedirect(reverse('manage'))
