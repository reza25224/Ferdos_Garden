from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from .models import Visitor_Group , Place


class VisitorGroup(CreateView):
    model=Visitor_Group
    fields='__all__'


class Place(CreateView):
    model=Place
    fields='__all__'