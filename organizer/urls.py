from django.urls import path
from .views import *

urlpatterns = [
    path('', OrganizerView.as_view(), name='organizer'), 
]

app_name = 'organizer'