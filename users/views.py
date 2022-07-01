from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import App

from .forms import SignUpForm


def signup_view(request):
	if request.user.is_authenticated:
		return redirect('users:dashboard')
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('users:dashboard')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = SignUpForm()

	return render(request, 'app/signup.html', {'form': form})


@login_required
def dashboard_view(request):
	apps = App.objects.all()
	return render(request, 'app/dashboard.html', {"apps": apps})


def home_view(request):
	if request.user.is_authenticated:
		return redirect('users:dashboard')
	return render(request, 'app/home.html')
