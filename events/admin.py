from django.contrib import admin
from .models import Event, Event_Registration

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'cost', 'booked_spots', 'max_capacity', 'published') # noqa
    ordering = ['time', 'title']


@admin.register(Event_Registration)
class Event_Registration_Admin(admin.ModelAdmin):
    list_display = ('event_title', 'event_time', 'user_full_name', 'confirmed', 'created_on') # noqa
    readonly_fields = ('created_on',)
    ordering = ['event_time', 'event_title', 'user']
    list_filter = ['event_title', 'event_time']

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_full_name.short_description = 'User'
    user_full_name.admin_order_field = 'user__first_name'
