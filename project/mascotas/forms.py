from django import forms

from . import models


class MascotaCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.MascotaCategoria
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = "__all__"

        widgets = {
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "raza": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_actualizacion": forms.DateInput(attrs={"class": "form-control"}),
        }