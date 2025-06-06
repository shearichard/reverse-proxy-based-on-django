from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

