from django.shortcuts import render
from django.views.generic.list import ListView
from app7_dictionary.models import DictionaryCn

# Create your views here.


class DictionaryCnView(ListView):
    model = DictionaryCn
    template_name = "cndic.html"
