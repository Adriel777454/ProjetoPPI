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
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context

class CriarReservasView(LoginRequiredMixin,CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "finecap/form.html"
    success_url = reverse_lazy('listar_reservas')

    def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.data_cadastro = datetime.now()
        reserva.save()
        return super().form_valid(form)
    
class EditarReservasView(LoginRequiredMixin,UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "finecap/form.html"
    success_url = reverse_lazy('listar_reservas')

    def form_valid(self, form):
        reservat = form.save(commit=False)
        reservat.data_cadastro = datetime.now()
        reservat.save()
        return super().form_valid(form)

class DeletarReservasView(LoginRequiredMixin,DeleteView):
    model = Reserva
    template_name = "finecap/actions/confirm_delete.html"
    success_url = reverse_lazy('listar_reservas')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

class ListarStandsView(UserPassesTestMixin,ListView):
    model = Stand
    template_name = "finecap/stands.html"
    context_object_name = "stands"
    ordering = ['id']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context

    def test_func(self):
        return self.request.user.is_superuser

class CriarStandsView(UserPassesTestMixin,CreateView):
    model = Stand
    form_class = StandForm
    template_name = "finecap/form.html"
    success_url = reverse_lazy('listar_stands')

    def test_func(self):
        return self.request.user.is_superuser

class EditarStandsView(UserPassesTestMixin,UpdateView):
    model = Stand
    form_class = StandForm
    template_name = "finecap/form.html"
    success_url = reverse_lazy('listar_stands')

    def test_func(self):
        return self.request.user.is_superuser

class DeletarStandsView(UserPassesTestMixin,DeleteView):
    model = Stand
    template_name = "finecap/actions/confirm_delete.html"
    success_url = reverse_lazy('listar_stands')

    def test_func(self):
        return self.request.user.is_superuser