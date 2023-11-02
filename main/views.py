from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import *
from datetime import datetime

class ListarReservasView(LoginRequiredMixin,ListView):
    model = Reserva
    template_name = "finecap/index.html"
    context_object_name = "reservas"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context
