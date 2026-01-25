from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from notes.models import Note

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    def get_queryset(self):
        return Note.objects.for_user(self.request.user) # type: ignore


class NoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")
    success_message = "Nota criada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user # type: ignore
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note
    fields = ["title", "body"]
    success_url = reverse_lazy("note_list")
    success_message = "Nota atualizada com sucesso!"


class NoteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note_list")
    success_message = "Nota excluída com sucesso!"


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    success_url = reverse_lazy("note_list")