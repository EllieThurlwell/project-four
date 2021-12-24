# from django.shortcuts import render, reverse, get_object_or_404
# from django.views import generic, View
# from django.http.response import HttpResponseRedirect
# from django.views.generic.base import TemplateView
# from django.conf import settings
# from .models import Event, Booking
# from .forms import ContactForm, BookingForm


# class EventList(generic.ListView):
#     #view to render the Event objects, max 9 per page
#     model = Event

#     Event.objects.all()
#     template_name = 'events.html'


# class HomePage(TemplateView):
#     #view to render the homepage
#     template_name = 'index.html'


# def booking(request):
#     #view to render the Booking form to booking.html
#     booking_form = None
#     # current_user = request.user
#     # booking_form = BookingForm(initial={'user': current_user.username})
#     if request.method == 'POST':
#         booking_form = BookingForm(data=request.POST)
#         # tried here
#         if booking_form.is_valid():
#             # tried here
#             booking_form = booking_form.save()
#             return HttpResponseRedirect(reverse('booking'))
#     else:
#         booking_form = BookingForm()

#     context = {'booking_form': booking_form}

#     return render(request, 'booking.html', context)
    
#     model = Booking
#     booked_run = Booking.objects.create(
#         user=request.user,
#         first_name=fname,
#         last_name=lname,
#         email=email,
#         date=date
#     )
#     booked_run.save()

# def contact(request):
#     #view to render the Contact form to contact.html
#     contact_form = None
#     if request.method == 'POST':    
#         contact_form = ContactForm(data=request.POST)
#         if contact_form.is_valid():
#             contact = contact_form.save()
#             return HttpResponseRedirect(reverse('contact'))
#     else:
#         contact_form = ContactForm()

#     context = {'contact_form': contact_form}

#     return render(request, 'contact.html', context)
    
  
# class ManageBooking(generic.ListView):
#     #view to render the manage booking page for logged in user
#     model = Booking
#     context_object_name = 'runs'
#     paginate_by = 6
#     template_name = 'manage.html'

#     def get_queryset(self):
#         return Booking.objects.filter(user=self.request.user)


# class EditBooking(View):
#     #view to edit a specific booking
#     def get(self, request, id):
#         queryset = Booking.objects.filter(user=request.user)
#         run = get_object_or_404(queryset, id=id)
#         context = {'edit_booking_form': BookingForm(instance=run)}

#         return render(request, 'edit-booking.html', context)

#     def post(self, request, id):
#         queryset = Booking.objects.filter(user=request.user)
#         run = get_object_or_404(queryset, id=id)
#         edit_booking_form = BookingForm(request.POST, instance=run)

#         if edit_booking_form.is_valid():
#             edit_booking_form.save()

#         else:
#             edit_booking_form = BookingForm(instance=run)

#         return render(request, 'manage.html')



# def delete_booking(request, id):
#     #view to delete a specific booking
#     queryset = Booking.objects.filter(user=request.user)
#     run = get_object_or_404(queryset, id=id)

#     run.delete()

#     return HttpResponseRedirect(reverse('manage'))


from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.conf import settings
from .models import Event, Booking
from .forms import ContactForm, BookingForm


class HomePage(TemplateView):
    #view to render the homepage
    template_name = 'index.html'
    
class EventList(generic.ListView):
    #view to render the Event objects, max 9 per page
    model = Event

    Event.objects.all()
    template_name = 'events.html'


def booking(request):
    #view to render the Booking form to booking.html
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
            return HttpResponseRedirect(reverse('booking'))
    else:
        booking_form = BookingForm()

    context = {'booking_form': booking_form}

    return render(request, 'booking.html', context)


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


class EditBooking(View):
    def get(self, request, id):
        queryset = Booking.objects.filter(user=request.user)
        run = get_object_or_404(queryset, id=id)
        return render(request, 'edit-booking.html', {'edit_booking_form': BookingForm(instance=run)})

    def post(self, request, id):
        queryset = Booking.objects.filter(user=request.user)
        run = get_object_or_404(queryset, id=id)
        edit_booking_form = BookingForm(request.POST, instance=run)

        if edit_booking_form.is_valid():
            edit_booking_form.save()
            return HttpResponseRedirect(reverse('manage'))
            
        return render(request, 'edit-booking.html', {'edit_booking_form': BookingForm(instance=run)})

def delete_booking(request, id):
    #view to delete a specific booking
    queryset = Booking.objects.filter(user=request.user)
    run = get_object_or_404(queryset, id=id)

    run.delete()
    return HttpResponseRedirect(reverse('manage'))





