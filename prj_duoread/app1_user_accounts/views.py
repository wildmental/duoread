"""views.py in app1_user_accounts"""
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone

from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from app1_user_accounts.models import UserAccount
from app1_user_accounts.forms import LoginForm
from app1_user_accounts.forms import RegisterForm
from app1_user_accounts.forms import ProfileChangeForm
# from django.contrib.auth.forms import UserChangeForm


def userinfo(request):
    """this is userinfo"""
    res_data = {}
    user = request.session.get('user_id')
    if user:
        account = UserAccount.objects.get(pk=user)
        res_data['username'] = account.username
        res_data['nickname'] = account.nickname
        res_data['birthdate'] = account.birthdate
    return render(request, 'user_info.html', res_data)


def logout(request):
    """this is a logout part"""
    if request.session.get('user_id'):
        del request.session['user_id']
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

# Need to leatn UpdateView usage


class ModelUpdateView(UpdateView):
    model = UserAccount
    form_class = ProfileChangeForm
    template_name = "user_update.html"
    success_url = '/account/info/'

    def get_object(self):
        return get_object_or_404(UserAccount, pk=self.request.session['user_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session['user_id']
        context["username"] = UserAccount.objects.get(pk=user_id).username
        context["nickname"] = UserAccount.objects.get(pk=user_id).nickname
        context["birthdate"] = UserAccount.objects.get(pk=user_id).birthdate
        return context

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update(
            {'request': self.request}
        )
        return kw
