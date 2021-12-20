from django.shortcuts import render
from django.views import generic, View
from django.views.generic.base import TemplateView
from .models import Event
from .forms import ContactForm

class EventList(generic.ListView):
    #view to render the Event objects, max 9 per page
    model = Event

    Event.objects.all()
    template_name = 'events.html'


class HomePage(TemplateView):
    #view to render the homepage
    template_name = 'index.html'


def contact(request):
    #view to render the Contact form to contact.html
    contact_form = None
    # forms displays if send clicked. need a get method first?
    if request.method == 'POST':    
        contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
        contact_form.instance.fname = request.user.fname
        contact_form.instance.lname = request.user.lname
        contact_form.instance.email = request.user.email
        message = contact_form.save(commit=False)
        message.save()
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})


# class Contact(TemplateView):
#     #view to render the Contact form to contact.html

#     # forms displays if send clicked. need a get method first?
#     def post(self, request):

#         contact_form = ContactForm(data=request.POST)
#         if contact_form.is_valid():
#             message = contact_form.save()
#         else:
#             contact_form = ContactForm()

#         return render(
#             request,
#             'contact.html',
#             {
#                 'contact_form': contact_form
#             },
#         )

#     template_name = 'contact.html'
