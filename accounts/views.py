from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'f': form})


def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
