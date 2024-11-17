from django.contrib import admin
from organizer.models import *

# Register your models here.

class OrganizerAdmin(admin.ModelAdmin):
    model = organizer

    list_display = ['organizer_id', 'organizer_name', 'organizer_address', 'external']
    ordering = ('organizer_id', )

class ContactPersonAdmin(admin.ModelAdmin):
    model = contactperson

    list_display = ['organizer_id', 'contact_name']
    ordering = ('organizer_id', )

admin.site.register(organizer, OrganizerAdmin)
admin.site.register(contactperson, ContactPersonAdmin)