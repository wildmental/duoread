"""views.py in app3_wordbook"""
from django.shortcuts import render
from .forms import WordmemoForm
# Create your views here.


def wordbook(request):
    """this is a wordbook part"""
    form = WordmemoForm()
    return render(request, 'wordbook.html', {'form': form})
