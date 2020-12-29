from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

# Create your views here.


class LangInit(FormView):
    pass


class LangSet(UpdateView):
    pass


class AppSet(UpdateView):
    pass
