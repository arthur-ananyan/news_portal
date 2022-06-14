from django.urls import path
from .views import LoginView, LogoutView, LandingPageView, SignUpView, MainPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(), name='login'),
    path('main/', MainPageView.as_view(), name='main'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
