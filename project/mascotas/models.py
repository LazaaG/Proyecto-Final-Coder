from django.db import models
from django.utils import timezone


class MascotaCategoria(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "categoría de mascotas"
        verbose_name_plural = "categorias de mascotas"

    def __str__(self) -> str:
        return self.nombre


class Mascota(models.Model):

    categoria = models.ForeignKey(
        MascotaCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría"
    )
    nombre = models.CharField(max_length=200)
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self) -> str:
        return f"{self.nombre} {self.raza}"