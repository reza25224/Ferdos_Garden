from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Visitor_Group , Place
from django.urls import reverse

#-------------------------------------------------------------------------
class VisitorGroup(CreateView):
    model=Visitor_Group
    fields='__all__'

#-------------------------------------------------------------------------Place Create
class PlaceCreate(CreateView):
    model=Place
    fields='__all__'
    # success_url='/introduction/list/'
    def get_success_url(self):
        return reverse('Placelist')

#----------------------------------------PLace List
class Placelist(ListView):
    model=Place

#----------------------------------------Place Detail
class PlaceDetail(DetailView):
    model=Place

#----------------------------------------Place Update
class PlaceUpdate(UpdateView):
    model=Place
    fields='__all__'
    success_url='/introduction/list/'
    
#----------------------------------------Place Delete
class PlaceDelete(DeleteView):
    model=Place
    success_url='/introduction/list/'