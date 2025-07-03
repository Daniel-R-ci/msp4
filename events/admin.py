from django.contrib import admin
from .models import Event, Event_Registration

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'cost', 'max_capacity', 'published')
    ordering = ['time', 'title']


@admin.register(Event_Registration)
class Event_Registration_Admin(admin.ModelAdmin):
    list_display = ('event_title', 'event_time', 'user')
    ordering = ['event_time', 'event_title']
