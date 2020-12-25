"""forms for user accounts"""
from django import forms
from .models import WordMemoCn


class WordmemoForm(forms.Form):
    """Wordmemo Form"""
    wordmemo = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '단어 메모 입력'}),
        error_messages={
            'required': '메모가 입력되지 않았습니다.'
        },
        label='단어 메모'
    )

    class Meta:
        model = WordMemoCn
        fields = ['wordmemo']

    def clean(self):
        cleaned_data = super().clean()
        wordmemo = cleaned_data.get('wordmemo')

        if wordmemo:
            self.wordmemo = wordmemo
