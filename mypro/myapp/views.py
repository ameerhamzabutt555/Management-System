from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from myapp.forms import CustomUserCreationForm

class BasePage(TemplateView):
    template_name = 'myapp/base.html'

class DashBoardPage(TemplateView):
    template_name = 'myapp/dashboard.html'

def register(request):
    if request.method == "GET":
        return render(
            request, "myapp/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))