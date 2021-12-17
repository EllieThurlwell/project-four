from django.db import models
from django.contrib.auth.models import User

DAYS = ((0, "Tuesday"), (1, "Thursday"), (2, "Saturday"))
LEVELS = ((0, "Beginner"), (1, "Intermediate"), (2, "Push yourself"))

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200, unique=True)
    day = models.IntegerField(choices=DAYS)
    level = models.IntegerField(choices=LEVELS)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Booking(models.Model):
    fname = models.CharField(max_length=200) #unique=False?
    lname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    option = models.IntegerField(choices=LEVELS, default=0)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        output = self.fname + self.lname + '-' + self.email
        return output

class Contact(models.Model):
    fname = models.CharField(max_length=200) #unique=False?
    lname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.message
