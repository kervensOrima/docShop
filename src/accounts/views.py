import logging

from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

User = get_user_model()


# Create your views here.
def sign_up(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            check_user = User.objects.get(username=username)
            if not check_user:
                user = User.objects.create_user(username=username, password=password)
                if user:
                    login(request=request, user=user)
                    return redirect('store:index')
            else:
                logging.error("username already exist, try with another one.")
                context['username_error'] = "username already exist, try with another one."

        except Exception as e:
            logging.error(e)

    context['title'] = 'Creation d un compte sur le site!'
    return render(request=request, template_name="accounts/signup.html", context=context)


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('store:index')


def sign_in(request: HttpRequest) -> HttpResponse:
    context = {}
    # template = loader.get_template(template_name="accounts/login.html")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('store:index')
            else:
                context['login_error'] = "username or password is invalid!!!"
                context['username'] = request.POST.get('username')
        except Exception as e:
            logging.error(e)

    context['title'] = 'login to your account'
    return render(request=request, template_name="accounts/login.html", context=context)
