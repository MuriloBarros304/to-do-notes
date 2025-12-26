from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todo, Note

# Todos

class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_as_finished()
        return redirect("todo_list")
    
# Notes

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"


class NoteCreateView(CreateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")
    template_name = "notes/note_form.html"


class NoteUpdateView(UpdateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")
    template_name = "notes/note_form.html"


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note_list")
    template_name = "notes/note_confirm_delete.html"