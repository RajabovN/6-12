from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, ProfileUpdateForm

class LoginRequiredMixin:
    def check_authentication(self, request):
        if not request.user.is_authenticated:
            return redirect("login")

class AuthenticationMixin:
    def login_user(self, request):
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("profile")
        else:
            form = LoginForm()
        return render(request, "registration/login.html", {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form})


def login_user(request):
    mixin = AuthenticationMixin()
    return mixin.login_user(request)


def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    mixin = LoginRequiredMixin()
    redirect_response = mixin.check_authentication(request)
    if redirect_response:
        return redirect_response
    return render(request, "registration/profile.html", {'user': request.user})


def profile_update(request):
    mixin = LoginRequiredMixin()
    redirect_response = mixin.check_authentication(request)
    if redirect_response:
        return redirect_response

    user = request.user
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, "registration/profile_update.html", {'form': form})


# Create your views here.
