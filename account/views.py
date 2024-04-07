from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm


def register_view(request):
    user = request.user

    if user.is_authenticated:
        # TODO redirect to Dashboard
        return redirect("dataGather:index")

    if request.user.is_authenticated:
        # TODO redirect must change to Login
        return redirect("dataGather:index")
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():

            # TODO compare pass1 and 2

            form.save()
            cd = form.cleaned_data
            username = cd["username"]
            email = cd["email"]
            password1 = cd["password1"]
            password2 = cd["password2"]

            acc = authenticate(email=email, password=password1)

            if acc:
                login(request, acc)
                # TODO redirect must change to Login
                return redirect("dataGather:index")
    else:
        form = RegistrationForm()
    return render(request,
                  "account/register.html",
                  {"form": form})


def login_view(request):
    user = request.user
    # TODO redirect to dashboard
    if user.is_authenticated:
        return redirect("dataGather:index")

    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd["email"]
            password = cd["password"]

            acc = authenticate(email=email, password=password)
            if acc:
                login(request, acc)
                # TODO redirect to dashboard
                return redirect("dataGather:index")
    else:
        form = LoginForm()
    return render(request,
                  "account/login.html",
                  {"form": form})


def logout_view(request):
    logout(request)
    return redirect("dataGather:index")
