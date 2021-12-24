from django.contrib import admin
from .models import Event, Contact, Booking


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'day', 'level', 'location')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'date')
