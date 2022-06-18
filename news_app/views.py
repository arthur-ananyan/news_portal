from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .forms import UserRegisterForm
from .azatutyun import get_news_azatutyun
from .models import NewsSubscription


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


class MainPageView(ListView):
    template_name = 'main.html'
    context_object_name = 'news'

    def get_queryset(self):
        return get_news_azatutyun()


class Subscriptions(ListView):
    model = NewsSubscription
    context_object_name = 'subscription'
    template_name = 'my_pages.html'
