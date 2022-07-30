from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView,DeleteView

from .models import Snack


# Create your views here.

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks_list"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    context_object_name = "snack_detail"


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    fields = ["title", "purchaser", "description"]
    model = Snack


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    fields = ["title", "purchaser", "description"]
    model = Snack


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    url = reverse_lazy("snacks_list")