"""views.py in app3_wordbook"""
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render
from app3_wordbook.models import UserWordsCn
from app7_dictionary.models import DictionaryCn


def wordbook(request):
    """this is a wordbook part"""
    form = WordmemoForm()
    return render(request, 'wordbook.html', {'form': form})


class WordBookCn(ListView):
    model = UserWordsCn
    template_name = "wordbook_cn.html"
    # paginate_by = 100
    context_object_name = 'wordbook'

    def get_queryset(self):
        user = self.request.user
        queryset = {
            'words': UserWordsCn.objects.all().filter(user_id=user.id)
        }
        return queryset


class WordAdd(FormView):
    pass


class WordDetail(DetailView):
    pass


class WordUpdate(UpdateView):
    pass
