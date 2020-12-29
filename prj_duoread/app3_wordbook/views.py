"""views.py in app3_wordbook"""
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render
from .forms import WordmemoForm

# Create your views here.


def wordbook(request):
    """this is a wordbook part"""
    form = WordmemoForm()
    return render(request, 'wordbook.html', {'form': form})


class WordList(ListView):
    pass


class WordAdd(FormView):
    pass


class WordDetail(DetailView):
    pass


class WordUpdate(UpdateView):
    pass
