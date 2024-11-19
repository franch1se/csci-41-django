from django.contrib import admin
from .models import *

# Register your models here.

class AddressInline(admin.TabularInline):
    model = address

class OrganizerAdmin(admin.ModelAdmin):
    model = organizer

    list_display = ['organizer_id', 'organizer_name', 'organizer_address', 'external']
    ordering = ('organizer_id', )

    inlines = [AddressInline, ]

class ContactPersonAdmin(admin.ModelAdmin):
    model = contact_person

    list_display = ['organizer_id', 'contact_name']
    ordering = ('organizer_id', )

class ActivityAdmin(admin.ModelAdmin):
    model = activity

class ActivityHostingAdmin(admin.ModelAdmin):
    model = activity_hosting

class ActivityBookingsAdmin(admin.ModelAdmin):
    model = activity_bookings

class ParticipantAdmin(admin.ModelAdmin):
    model = participant

class ParticipantTypeAdmin(admin.ModelAdmin):
    model = participant_type



admin.site.register(organizer, OrganizerAdmin)
admin.site.register(contact_person, ContactPersonAdmin)
admin.site.register(activity, ActivityAdmin)
admin.site.register(activity_hosting, ActivityHostingAdmin)
admin.site.register(activity_bookings, ActivityBookingsAdmin)
admin.site.register(participant, ParticipantAdmin)
admin.site.register(participant_type, ParticipantTypeAdmin)