from .models import Contact, Booking
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fname', 'lname', 'email', 'message',)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        date = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )
        fields = ('user', 'fname', 'lname', 'email', 'date',) #date validity?
