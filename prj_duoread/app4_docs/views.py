"""user docs view control"""
from django.shortcuts import render
from django.db.models import Count

from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from app4_docs.models import UserDocs
from app4_docs.forms import DocCreationText
from app4_docs.forms import DocCreationFile
from app4_docs.forms import DocCreationImage

# Create your views here.


class DocCreationTextView(FormView):
    model = UserDocs
    form_class = DocCreationText
    template_name = "doc_create.html"
    success_url = "/"  # "/docs/list/"

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update(
            {'request': self.request}
        )
        return kw


class DocCreationFileView(FormView):
    model = UserDocs
    form_class = DocCreationFile
    template_name = "doc_create.html"
    success_url = "/"  # "/docs/list/"

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update(
            {'request': self.request}
        )
        return kw


class DocCreationImageView(FormView):
    model = UserDocs
    form_class = DocCreationImage
    template_name = "doc_create.html"
    success_url = "/"  # "/docs/list/"

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update(
            {'request': self.request}
        )
        return kw


class DocList(ListView):
    model = UserDocs
    template_name = "doc_list.html"
    context_object_name = 'doc_list'

    def get_queryset(self):
        user = self.request.user
        all_docs = UserDocs.objects.all().filter(user_id=user.id).defer(
            'user_id', 'update_dt').order_by('id')
        queryset = {
            'all_docs': all_docs
        }
        return queryset


class Recent(ListView):
    pass


def docs_update(request, pk):
    """gets the original doc and allow user to revise them"""
    pass
