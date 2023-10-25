from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from . import forms

class MascotaCategoriaList(ListView):
    model = MascotaCategoria

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = MascotaCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = MascotaCategoria.objects.all()
        return object_list


class MascotaCategoriaDetail(DetailView):
    model = MascotaCategoria


class MascotaCategoriaCreate(CreateView, LoginRequiredMixin):
    model = MascotaCategoria
    form_class = forms.MascotaCategoriaForm
    success_url = reverse_lazy("mascota:mascotacategoria_list")


class MascotaCategoriaUpdate(UpdateView, LoginRequiredMixin):
    model = MascotaCategoria
    form_class = forms.MascotaCategoriaForm
    success_url = reverse_lazy("mascota:mascotacategoria_list")


class MascotaCategoriaDelete(DeleteView, LoginRequiredMixin):
    model = MascotaCategoria
    success_url = reverse_lazy("mascota:mascotacategoria_list")


class MascotaList(ListView):
    model = Mascota

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = Mascota.objects.filter(nombre__icontains=consulta)
        else:
            object_list = Mascota.objects.all()
        return object_list


class MascotaCreate(CreateView):
    model = Mascota
    form_class = forms.MascotaForm
    success_url = reverse_lazy("mascota:mascota_list")


class MascotaDetail(DetailView):
    model = Mascota


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = forms.MascotaForm
    success_url = reverse_lazy("mascota:mascota_list")

class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy("mascota:mascota_list")