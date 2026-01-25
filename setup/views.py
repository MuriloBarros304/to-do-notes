from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                if field == '__all__':
                    messages.error(self.request, error) # type: ignore
                else:
                    messages.error(self.request, f"{field.title()}: {error}")
        
        return super().form_invalid(form)
    
    success_message = "Conta criada com sucesso! Você já pode fazer login."


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"Bem-vindo, {user.username}!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Nome de usuário ou senha inválidos. Tente novamente.")
        return super().form_invalid(form)