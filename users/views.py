from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            message = "Invalid username or password"

    return render(request, "login.html", {"message": message})


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def profile(request):
    return render(request, "profile.html")