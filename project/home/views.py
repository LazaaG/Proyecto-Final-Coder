from django.shortcuts import render, redirect
from django.shortcuts import render
from . forms import *

def register(request):
    if request.method == 'POST':
        mi_formulario = UserCreationFormEspanol(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            user = mi_formulario.cleaned_data.get("username")
            return render(request, 'index.html')
        else:
            return render(request, "home/register.html")
    else:
        mi_formulario = UserCreationFormEspanol()
        return render(request, "home/register.html", {"mi_formulario": mi_formulario})
