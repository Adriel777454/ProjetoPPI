from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import *
from datetime import datetime
from django.db.models import Q

class ListarReservasView(LoginRequiredMixin,ListView):

    model = Reserva
    template_name = "finecap/index.html"
    context_object_name = "reservas"
    paginate_by = 3
    ordering = ["data_cadastro"]
    
    def get_queryset(self):
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = Reserva.objects.filter(nome_empresa__icontains=search_query)
        else:
            queryset = Reserva.objects.all()

        return queryset


    def get_queryset(self):
        filter_stand = self.request.GET.get('stand_filter', '')
        filter_quitado = self.request.GET.get('quitado_filter', '')

        queryset = Reserva.objects.all()

        # Use Q objects to combine filters
        filter_conditions = Q()

        if filter_quitado == "1":
            filter_conditions &= Q(quitado=True)
        if filter_quitado == "2":
            filter_conditions &= Q(quitado=False)

        stand_filters = {
            "1": "Front",
            "2": "Back",
            "3": "Left",
            "4": "Right",
        }

        if filter_stand in stand_filters:
            filter_conditions &= Q(stand__localizacao=stand_filters[filter_stand])

        # Apply the combined filter conditions to the queryset

        if filter_conditions:
            queryset = queryset.filter(filter_conditions)
        else:
            queryset = Reserva.objects.all()

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')

        # Adicione a search_query ao contexto para preencher automaticamente o campo de pesquisa
        context['search_query'] = search_query

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