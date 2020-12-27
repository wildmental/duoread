"""forms for tutor request"""
from django import forms
from .models import TutorRequest


class TutorReqForm(forms.Form):
    """tutor req form"""
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '질문 제목 입력'}),
        error_messages={
            'required': '제목은 필수 입력값입니다.'
        },
        label='제목')
    # 모르는 단어 선택하는 필드로 구현
    word1 = forms.CharField(widget=forms.TextInput())
    word2 = forms.CharField(widget=forms.TextInput())
    word3 = forms.CharField(widget=forms.TextInput())
    word4 = forms.CharField(widget=forms.TextInput())
    word5 = forms.CharField(widget=forms.TextInput())
    question_txt = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '질문 내용 입력'}),
        error_messages={
            'required': '본문을 입력해주세요.'
        },
        label='질문 내용')

    class Meta:
        model = TutorRequest
        fields = ['title', 'word1', 'word2', 'word3',
                  'word4', 'word5', 'question_txt']
