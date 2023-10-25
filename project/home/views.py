from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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


@login_required
def ver_perfil(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, 'perfil/ver_perfil.html', context)


@login_required    
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UsuarioEditForm(request.POST, instance=request.user)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data["password1"])
            usuario.save()
            return render(request, "index.html", {"mensaje": "Datos actualizados ;)"})
        else:
            return render(request, "index.html", {"mi_formulario": mi_formulario})
    else:
        mi_formulario = UsuarioEditForm(instance=request.user)
        return render(request, "perfil/editar_perfil.html", {"mi_formulario": mi_formulario})