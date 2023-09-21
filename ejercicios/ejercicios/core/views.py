from django.shortcuts import render, HttpResponse, redirect
from .forms import UsuarioForm



def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            return redirect('detalle_usuario', usuario_id=usuario.id)
    else:
        form = UsuarioForm()
    return render(request, 'agregar_usuario.html', {'form': form})
