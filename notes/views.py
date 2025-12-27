from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from notes.models import Note

class NoteListView(ListView):
    model = Note


class NoteCreateView(CreateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")


class NoteUpdateView(UpdateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note_list")


class NoteDetailView(DetailView):
    model = Note
    success_url = reverse_lazy("note_list")