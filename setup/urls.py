from django.contrib import admin
from django.urls import path
from todos.views import TodoListView, \
    TodoCreateView, TodoUpdateView, TodoDeleteView, \
    TodoCompleteView
from notes.views import NoteDetailView, NoteListView, \
    NoteCreateView, NoteUpdateView, NoteDeleteView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
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
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),

    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),
]
