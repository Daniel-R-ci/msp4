from django.db import models
from django.contrib.auth.models import User


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

    @property
    def booked_spots(self):
        booked_spots = Event_Registration.objects.filter(event=self).count()
        return booked_spots

    @property
    def available_spots(self):
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
