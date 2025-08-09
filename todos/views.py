from django.shortcuts import render

def todo_list(request):
    nome = "Murilo"
    return render(request, "todos/todo_list.html", {"nome": nome})
