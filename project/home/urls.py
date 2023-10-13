from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("login/", LoginView.as_view(template_name="home/login.html", next_page="index"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("about/", TemplateView.as_view(template_name="home/about.html"), name="about"),
    path("register/", views.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()