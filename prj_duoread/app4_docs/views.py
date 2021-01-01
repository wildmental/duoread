"""user docs view control"""
from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from app4_docs.models import UserDocs
from app10_subscription.models import Subscription
from app10_subscription.models import UsageLimits
# Create your views here.


class DocCreate(CreateView):
    model = UserDocs
    fields = '__all__'
    template_name = "doc_create.html"


class DocImport(FormView):
    pass


class DocList(ListView):
    pass


class Recent(ListView):
    pass


class ModelUpdateView(UpdateView):
    model = UserDocs
    template_name = "doc_update.html"
