from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'  
    next_page = reverse_lazy('login')


def logout_confirmation(request):
    return render(request, 'logout.html')

