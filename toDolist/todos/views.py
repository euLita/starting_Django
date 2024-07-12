from django.shortcuts import render

# Create your views here.
def todo_list(request):
    name = "Tali"
    alunos = ['Antonio Fonseca', 'Ana Beatriz', 'Jose Maria']
    return render(request,"todo_list.html", {'name': name, 'alunos': alunos})