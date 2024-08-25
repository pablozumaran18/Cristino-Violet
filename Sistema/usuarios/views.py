from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicio de sesión automatico para el registro
            return redirect('home')  # Redirige a la página de inicio o donde prefieras
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
