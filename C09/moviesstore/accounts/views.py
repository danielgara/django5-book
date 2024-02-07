from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import UserCreateForm

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def signup(request):
    templateData = {}
    templateData["title"] = "Sign Up"

    if request.method == 'GET':
        templateData["form"] = UserCreateForm()
        return render(request, 'accounts/signup.html', {"templateData": templateData})
    else:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                auth_login(request, user)
                return redirect('home.index')
            except IntegrityError as error:
                templateData["error"] = [error]
        else:
            error_list = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_list.append(error)

            templateData["error"] = error_list

        templateData["form"] = form
        return render(request, 'accounts/signup.html', {"templateData": templateData})

def login(request):
    templateData = {}
    templateData["title"] = "Login"
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {"templateData": templateData})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            templateData["error"] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {"templateData": templateData})
        else:
            auth_login(request, user)
            return redirect('home.index')