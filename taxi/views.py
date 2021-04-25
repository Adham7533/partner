from django.views.generic import ListView
from .models import Taxis
from rest_framework import generics
from taxi.models import Taxis


class TaxisListView(ListView):
    model = Taxis
    template_name = 'taxis_lis.html'

