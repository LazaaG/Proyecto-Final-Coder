from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "mascota"

urlpatterns = [
    path("", TemplateView.as_view(template_name="mascotas/index.html"), name="index"),
]

# MascotaCATEGORIA
urlpatterns += [
    path("mascotacategoria/list/", views.MascotaCategoriaList.as_view(), name="mascotacategoria_list"),
    path("mascotacategoria/create/", views.MascotaCategoriaCreate.as_view(), name="mascotacategoria_create"),
    path("mascotacategoria/detail/<int:pk>", views.MascotaCategoriaDetail.as_view(), name="mascotacategoria_detail"),
    path("mascotacategoria/update/<int:pk>", views.MascotaCategoriaUpdate.as_view(), name="mascotacategoria_update"),
    path("mascotacategoria/delete/<int:pk>", views.MascotaCategoriaDelete.as_view(), name="mascotacategoria_delete"),
]

# Mascota
urlpatterns += [
    path("mascota/list/", views.MascotaList.as_view(), name="mascota_list"),
    path("mascota/create/", views.MascotaCreate.as_view(), name="mascota_create"),
    path("mascota/detail/<int:pk>", views.MascotaDetail.as_view(), name="mascota_detail"),
    path("mascota/update/<int:pk>", views.MascotaUpdate.as_view(), name="mascota_update"),
    path("mascota/delete/<int:pk>", views.MascotaDelete.as_view(), name="mascota_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)