from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (
    DeleteView,CreateView,UpdateView
)
from app.filters import StudentFilter
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from .models import Record
# Create your views here.

class StudentListView(FilterView):
    model = Record
    template_name="home.html"
    filterset_class = StudentFilter 

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Record
    template_name= "record_new.html"
    fields = ["reg_no", "name", "vaccine_status"]
    success_url = reverse_lazy("record_new")
    success_message = "Record was added successfully"

class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Record
    template_name = "record_delete.html"
    success_url = reverse_lazy("home")
    success_message = "Record was deleted successfully"

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Record
    template_name= "record_edit.html"
    fields = ["reg_no", "name", "vaccine_status"]
    success_url = reverse_lazy("home")
    success_message = "Record was updated successfully"