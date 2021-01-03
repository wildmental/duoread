"""forms for user accounts"""
from django import forms
from django.utils.translation import gettext as _
from app3_wordbook.models import UserWordsCn
from django.forms.fields import validators


class UserWordsCnMemoForm(forms.ModelForm):
    """User Words Memo Form"""

    memo_txt = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('단어 메모 입력')}),
        label=_('단어 메모'),
        error_messages={
            'max_length': _('단어메모 최대 길이는 %(limit_value)d자 입니다.<br>(현재 입력 %(show_value)d자)'),
        },
        max_length=100,
        validators=[validators.MaxLengthValidator, ],
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()

    class Meta:
        model = UserWordsCn
        fields = ['memo_txt', ]
