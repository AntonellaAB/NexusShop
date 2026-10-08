from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroClienteForm


def home(request):
    return render(request, 'accounts/index.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroClienteForm()
    return render(request, 'accounts/registro.html', {'form': form})