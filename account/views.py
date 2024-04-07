from django.contrib.auth import login, password_validation, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm


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
