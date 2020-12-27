"""this is a home view"""
from django.shortcuts import render
# from django.http import HttpResponse
# from django.utils import timezone
# from app1_user_accounts.models import UserAccount


# Create your views here.


def home(request):
    """this is a home page"""
    # if session_id:
    #     user_account = UserAccount.objects.get(pk=session_id)
    return render(request, "home.html")
