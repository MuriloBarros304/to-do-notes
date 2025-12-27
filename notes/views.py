from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from notes.models import Note

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    def get_queryset(self):
        return Note.objects.for_user(self.request.user) # type: ignore


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note_list")


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    success_url = reverse_lazy("note_list")