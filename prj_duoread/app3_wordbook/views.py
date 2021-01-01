"""views.py in app3_wordbook"""
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

from app3_wordbook.models import UserWordsCn
from app3_wordbook.forms import UserWordsCnMemoForm
from app7_dictionary.models import DictCn


def mark_update(request, pk):
    """this is a wordbook part"""
    res_data = {}
    res_data['form'] = UserWordsCnMemoForm
    if request.method == 'POST':
        user = request.user
        if request.POST['word_mark'] != '':
            word_mark = request.POST['word_mark']
            userword = get_object_or_404(
                UserWordsCn, id=pk)
            userword.word_mark = word_mark
            userword.save()
            res_data['mark_edited'] = pk
            res_data['wordbook'] = {
                'words':
                UserWordsCn.objects.all().filter(user_id=user.id).order_by('id')
            }
        else:
            res_data['error'] = _("단어 구분이 전달되지 않았습니다.")
    return render(request, 'wordbook_cn.html', res_data)


def memo_update(request, pk):
    """this is a wordbook part"""
    res_data = {}
    res_data['form'] = UserWordsCnMemoForm
    if request.method == 'POST':
        form = UserWordsCnMemoForm(request.POST)
        user = request.user
        if not form.errors:
            userword = get_object_or_404(
                UserWordsCn, id=pk)
            if form.cleaned_data.get('memo_txt') != '':
                memo_update = form.cleaned_data.get('memo_txt')
                userword.memo_txt = memo_update
                userword.save()
            else:
                res_data['errors'] = _("빈 메모 입력시<br>기존 메모를 저장합니다.")
        else:
            print(form.errors)
            res_data['errors'] = form.errors
        res_data['mark_edited'] = pk
        res_data['wordbook'] = {
            'words':
            UserWordsCn.objects.all().filter(user_id=user.id).order_by('id')
        }
    return render(request, 'wordbook_cn.html', res_data)


class WordBookCn(ListView):
    model = UserWordsCn
    template_name = "wordbook_cn.html"
    # paginate_by = 100
    context_object_name = 'wordbook'

    def get_queryset(self):
        user = self.request.user
        queryset = {
            'words': UserWordsCn.objects.all().filter(user_id=user.id).order_by('id')
        }
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserWordsCnMemoForm
        return context


class WordAdd(FormView):
    pass


class WordDetail(DetailView):
    pass
