from django.contrib import admin
from django.urls import path
from todos.views import TodoListView, \
    TodoCreateView, TodoUpdateView, TodoDeleteView, \
    TodoCompleteView, NoteListView, NoteCreateView, \
    NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("todos/create", TodoCreateView.as_view(), name="todo_create"),
    path("todos/update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("todos/delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("todos/complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),

    path("notes/", NoteListView.as_view(), name="note_list"),
    path("notes/create", NoteCreateView.as_view(), name="note_create"),
    path("notes/update/<int:pk>", NoteUpdateView.as_view(), name="note_update"),
    path("notes/delete/<int:pk>", NoteDeleteView.as_view(), name="note_delete"),
]
