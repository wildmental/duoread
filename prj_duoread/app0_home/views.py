"""this is a home view"""
from django.shortcuts import render
# from django.http import HttpResponse
# from django.utils import timezone
from app1_user_accounts.models import UserAccount


# Create your views here.


def home(request):
    """this is a home page"""
    userid = request.session['user']
    if request.session.user:
        user_account = UserAccount.objects.get(pk=userid)
        return render(request, "member_home.html", user_account)
    else:
        return render(request, "welcome.html")
