from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'sent_on', 'read')
    ordering = ['read', 'sent_on',]
