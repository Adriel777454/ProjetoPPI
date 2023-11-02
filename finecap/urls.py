"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import ListarReservasView, CriarReservasView, DeletarReservasView, EditarReservasView, ListarStandsView, CriarStandsView, DeletarStandsView, EditarStandsView

urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('', ListarReservasView.as_view(), name="listar_reservas"),
    path('reserva/criar', CriarReservasView.as_view(), name="criar_reservas"),
    path('reserva/editar/<int:pk>/', EditarReservasView.as_view(), name="editar_reservas"),
    path('reserva/deletar/<int:pk>/', DeletarReservasView.as_view(), name="deletar_reservas"),

    path('stand/', ListarStandsView.as_view(), name="listar_stands"),
    path('stand/criar', CriarStandsView.as_view(), name="criar_stands"),
    path('stand/editar/<int:pk>/', EditarStandsView.as_view(), name="editar_stands"),
    path('stand/deletar/<int:pk>/', DeletarStandsView.as_view(), name="deletar_stands"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
