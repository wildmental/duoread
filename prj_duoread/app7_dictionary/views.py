from django.shortcuts import render
from django.views.generic.list import ListView
from app7_dictionary.models import DictCn
from app7_dictionary.models import DictEn

# Create your views here.


class DictCnView(ListView):
    model = DictCn
    template_name = "cndic.html"


class DictEnView(ListView):
    model = DictEn
    template_name = "endic.html"
