"""views.py in app1_user_accounts"""
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from app1_user_accounts.models import UserAccount
from app1_user_accounts.forms import LoginForm
from app1_user_accounts.forms import RegisterForm
from app1_user_accounts.forms import UserUpdateForm


def userinfo(request):
    """this is userinfo"""
    user = request.session.get('user_id')
    if user:
        account = UserAccount.objects.get(pk=user)
    return render(request, 'user_info.html')


def log_out(request):
    """this is a logout part"""
    logout(request)
    return redirect('/')


def log_in(request):
    """this is a login part"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    """this is a member registration"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.errors:
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
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})


class ModelUpdateView(UpdateView):
    model = UserAccount
    form_class = UserUpdateForm
    template_name = "user_update.html"
    success_url = '/account/info/'

    def get_object(self):
        user_id = self.request.user.id
        return get_object_or_404(UserAccount, pk=user_id)

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update(
            {'request': self.request}
        )
        return kw
