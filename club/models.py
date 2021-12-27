from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

DAYS = ((0, "Tuesday"), (1, "Thursday"), (2, "Saturday"))
LEVELS = ((0, "Beginner"), (1, "Intermediate"), (2, "Push yourself"))

#schema for Event model
class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    day = models.IntegerField(choices=DAYS)
    level = models.IntegerField(choices=LEVELS)
    location = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

#schema for Booking model
class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.email} booked on {self.date}"

#schema for Contact model of contact form
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return f"{self.message} from {self.email}"
