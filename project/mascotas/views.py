from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class MascotaCategoriaList(ListView):
    model = models.MascotaCategoria

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.MascotaCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.MascotaCategoria.objects.all()
        return object_list


class MascotaCategoriaDetail(DetailView):
    model = models.MascotaCategoria


class MascotaCategoriaCreate(CreateView, LoginRequiredMixin):
    model = models.MascotaCategoria
    form_class = forms.MascotaCategoriaForm
    success_url = reverse_lazy("mascota:mascotacategoria_list")


class MascotaCategoriaUpdate(UpdateView, LoginRequiredMixin):
    model = models.MascotaCategoria
    form_class = forms.MascotaCategoriaForm
    success_url = reverse_lazy("mascota:mascotacategoria_list")


class MascotaCategoriaDelete(DeleteView, LoginRequiredMixin):
    model = models.MascotaCategoria
    success_url = reverse_lazy("mascota:mascotacategoria_list")


class MascotaList(ListView):
    model = models.Mascota

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Mascota.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Mascota.objects.all()
        return object_list


class MascotaCreate(CreateView):
    model = models.Mascota
    form_class = forms.MascotaForm
    success_url = reverse_lazy("mascota:mascota_list")


class MascotaDetail(DetailView):
    model = models.Mascota


class MascotaUpdate(UpdateView):
    model = models.Mascota
    form_class = forms.MascotaForm
    success_url = reverse_lazy("mascota:mascota_list")


class MascotaDelete(DeleteView):
    model = models.Mascota
    success_url = reverse_lazy("mascota:mascota_list")