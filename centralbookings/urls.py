from django.urls import path
from .views import *

urlpatterns = [
    path('organizer', OrganizerView.as_view(), name='organizer'), 
]

app_name = 'centralbookings'