"""
app message views
NOT USED AT ALL (USE THE MEMBER's NAV BAR)
"""
from django.shortcuts import render
from django.views.generic.list import ListView
from app6_message.models import MessageLog

# Create your views here.


class MsgList(ListView):
    model = MessageLog
    pass
