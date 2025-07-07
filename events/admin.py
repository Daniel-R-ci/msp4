from django.contrib import admin
from .models import Event, Event_Registration

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'cost', 'booked_spots', 'max_capacity', 'published') # noqa
    ordering = ['time', 'title']


@admin.register(Event_Registration)
class Event_Registration_Admin(admin.ModelAdmin):
    list_display = ('event_title', 'event_time', 'user', 'confirmed', 'created_on') # noqa
    readonly_fields = ('created_on',)
    ordering = ['event_time', 'event_title', 'user']
    list_filter = ['event_title', 'event_time']
