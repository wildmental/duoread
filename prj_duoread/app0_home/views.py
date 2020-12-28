"""this is a home view"""
from django.shortcuts import render
# from django.http import HttpResponse
# from django.utils import timezone
from app1_user_accounts.models import UserAccount


# Create your views here.


def home(request):
    """this is a home page"""
    res_data = {}
    try:
        user = request.session['user']
        if user:
            user_account = UserAccount.objects.get(pk=user)
            res_data['username'] = user_account.username
            res_data['nickname'] = user_account.nickname
            return render(request, "member_home.html", res_data)
    except Exception:
        user = None
        error = Exception.__dict__
        res_data['error'] = error
    return render(request, "welcome.html", res_data)
