"""forms for user accounts"""
from django import forms
from app3_wordbook.models import UserWordsCn


class UserWordsCnForm(forms.Form):
    """User Words Marking Form"""

    word_mark = forms.ChoiceField(
        choices=('V', 'U', 'K', 'C'),
        label='단어 분류'
    )
    memo_txt = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '단어 메모 입력'}),
        error_messages={
            'required': '메모가 입력되지 않았습니다.'
        },
        label='단어 메모'
    )

    class Meta:
        model = UserWordsCn
        fields = ['word_mark', 'memo_txt']
