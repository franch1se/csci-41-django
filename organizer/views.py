from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import FormView
from django.urls import reverse_lazy

# Create your views here.

result = []
name_result = 'Name'

class OrganizerView(FormView):
    model = organizer
    form_class = OrganizerForm
    template_name = 'organizer.html'

    def get_success_url(self) -> str:
        return reverse_lazy('organizer:organizer')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        context = super().get_context_data(**kwargs)
        if form.is_valid():
            name_result = str(request.POST['organizer_name'])
            print(name_result)
            context['results'] = sql_query(0, name_result)
        return render(request, 'organizer.html', context)
    
    def get_context_data(self, **kwargs: reverse_lazy):
        context = super().get_context_data(**kwargs)
        context['results'] = result
        return context
    
def sql_query(query: int, name):
    result = []
    if query == 0:
        result = organizer.objects.raw("SELECT o.organizer_id, c.organizer_id_id, o.organizer_name AS name, o.organizer_address AS address, c.contact_name AS contact, c.contact_email AS email, c.contact_phone_number AS contact_no FROM organizer_organizer AS o INNER JOIN organizer_contactperson AS c ON o.organizer_id=c.organizer_id_id WHERE o.organizer_name=%(name)s", {'name': name})
    return result
# SOURCES
# https://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python#902417