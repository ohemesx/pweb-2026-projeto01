from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def elenco(request):
    return render(request, 'elenco.html')

def sobre(request):
    return render(request, 'sobre.html')