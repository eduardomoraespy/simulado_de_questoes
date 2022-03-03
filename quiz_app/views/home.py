from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def quiz(request):
    return render(request, 'quiz.html')

def tipo_de_prova(request):
    
    # Separar por simulado completo ou materias isoladas.
    
    pass