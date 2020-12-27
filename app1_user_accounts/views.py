"""views.py in app1_user_accounts"""
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse

from app1_user_accounts.models import UserAccount
from app1_user_accounts.forms import LoginForm
from app1_user_accounts.forms import RegisterForm


def logout(request):
    """this is a logout part"""
    if request.session.get('user_id'):
        del request.session['user_id']
        del request.session['session_id']
    return redirect('/')


def login(request):
    """this is a login part"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # temporary session code
            request.session['user_id'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    """this is a member registration"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        errors = form.errors
        if not errors:
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            birthdate = form.cleaned_data.get('birthdate')
            password = form.cleaned_data.get('password1')
            UserAccount.objects.create_user(
                username, nickname, password, birthdate=birthdate
            )
            print('[' + str(timezone.datetime.now()) + '] ' +
                  '<UserAccount : %s> registered' % nickname)
            return render(request, 'registered.html', {"result": nickname})
    else:
        errors = {}
        form = RegisterForm()
    return render(request, 'register.html', {"form": form, "errors": errors})
