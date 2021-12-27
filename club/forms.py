from .models import Contact, Booking
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'date',)

    date = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
