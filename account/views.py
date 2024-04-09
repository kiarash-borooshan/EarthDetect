from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, AccountUpdateForm
from .models import Account


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


def edit_account_view(request, pk):

    # TODO warning when password is not correct
    # TODO titles in templates html cannot change to persian

    account = Account.objects.get(pk=pk)
    if not request.user.is_authenticated:
        return redirect("account:login")
    if request.POST:
        form = AccountUpdateForm(data=request.POST,
                                 files=request.FILES,
                                 instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("account:edit_profile", pk=account.pk)

    else:
        form = AccountUpdateForm(initial={
            "id": account.pk,
            "email": account.email,
            "username": account.username,
            "profile_image": account.profile_image
        })
    return render(request,
                  "account/edit_profile.html",
                  {"form": form,
                   "account": account})
