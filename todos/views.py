from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    def get_queryset(self):
        return Todo.objects.for_user(self.request.user) # type: ignore


class TodoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    success_message = "Tarefa criada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user # type: ignore
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    success_message = "Tarefa atualizada com sucesso!"


class TodoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    success_message = "Tarefa excluída com sucesso!"

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_as_finished()
        return redirect("todo_list")