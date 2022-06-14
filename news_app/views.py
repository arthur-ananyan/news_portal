from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main')


class LogoutView(LogoutView):
    success_url = 'home.html'


class LandingPageView(TemplateView):
    template_name = 'home.html'


class MainPageView(TemplateView):
    template_name = 'main.html'
