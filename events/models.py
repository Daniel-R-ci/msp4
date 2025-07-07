from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    max_capacity = models.IntegerField()
    cost = models.FloatField()
    publish_on = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # Retrieves number of reserved spots for event
    # Includes booking being made (5-minute limit)
    @property
    def booked_spots(self):
        """
        Retrieves number of reserved spots for event
        """

        # Remove all uncofirmed bookings older than 5 minutes
        Event_Registration.remove_unconfirmed_registrations()

        # Count reservations for this event
        booked_spots = Event_Registration.objects.filter(event=self).count()
        return booked_spots

    # Retrieves number of available spots for event
    @property
    def available_spots(self):
        """
        Retrieves number of available spots for event
        """
        return self.max_capacity - self.booked_spots


class Event_Registration(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        related_name='participant')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses')
    created_on = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    event_title = models.CharField(max_length=255)
    event_time = models.DateTimeField()
    event_cost = models.FloatField()

    def __str__(self):
        return self.event_title

    # Remove all registrations that has not been confirmed after five minutes
    @staticmethod
    def remove_unconfirmed_registrations():
        """
        Remove all event registrations that has not been
        confirmed within five minutes
        """
        cutoff_time = timezone.now() - timedelta(minutes=1)
        Event_Registration.objects.filter(
            created_on__lt=cutoff_time, confirmed=False).delete()
