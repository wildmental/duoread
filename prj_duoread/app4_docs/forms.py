"""forms for documents"""
from django import forms
from django.utils.timezone import datetime
from django.utils.translation import gettext as _
from app4_docs.models import UserDocs
from django.forms.fields import validators


class DocCreationText(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    """document creation from text"""
    doc_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('문서 제목 입력')}),
        label=_('문서 제목'),
        error_messages={
            'max_length': _('문서 제목의 최대 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)'),
        },
        help_text=_('제목란을 비워 둘 경우 "연번(책장별)/문서첫단어/날짜"로 자동 설정됩니다.'),
        max_length=64,
        validators=[validators.MaxLengthValidator, ],
        required=False
    )
    doc_txt = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _(
            '문서 내용을 여기에 복사해 넣으세요 (최대 길이 1,000자)')}),
        label=_('문서 내용'),
        error_messages={
            'max_length': _('텍스트 입력 최대 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)'),
            'required': _('문서 내용란은 공란으로 남겨둘 수 없습니다.')
        },
        help_text=_(
            '1,000자를 초과하는 문서는 <a href="/docs/create/file/">파일로 불러오기</a>를 이용하세요.'),
        max_length=1000,
        validators=[validators.MaxLengthValidator, ],
        required=True
    )
    # choice field
    DEFAULT = 'DF'
    CASUAL = 'CA'
    NEWS = 'NA'
    LITERATURE = 'LI'
    ACADEMIC = 'AC'
    DOC_GROUP_CHOICES = [
        (DEFAULT, _('기본 책장')),
        (CASUAL, _('일상(SNS 등)')),
        (NEWS, _('뉴스기사')),
        (LITERATURE, _('문학')),
        (ACADEMIC, _('학술'))
    ]
    doc_group = forms.ChoiceField(
        choices=DOC_GROUP_CHOICES,
        label=_('보관할 책장 선택'),
        help_text=_('미선택시 기본 책장으로 자동 설정됩니다.'),
    )

    def clean(self):
        cleaned_data = super().clean()
        user = self.request.user
        doc_title = cleaned_data.get('doc_title')
        doc_txt = cleaned_data.get('doc_txt')
        doc_group = cleaned_data.get('doc_group')
        if doc_txt is None:
            pass
        else:
            if doc_title == '':
                try:
                    user_docs = UserDocs.objects.all().filter(user_id=user)
                    shelf_requested = user_docs.filter(doc_group=doc_group)
                    docnum = shelf_requested.count()+1
                except UserDocs.DoesNotExist:
                    docnum = 1
                finally:
                    dt = str(datetime.now().date())
                    first_word = doc_txt.split(' ')[0] if len(
                        doc_txt.split(' ')[0]) <= 10 else doc_txt.split(' ')[0][0:10]
                    doc_title = '/'.join([str(docnum), first_word, dt])
            if doc_group is None:
                self.add_error('doc_group', _("알수없는 이유로 책장이 선택되지 않았습니다."))
            else:
                created_doc = UserDocs(user_id=user,
                                       doc_title=doc_title,
                                       doc_txt=doc_txt,
                                       doc_group=doc_group)
                created_doc.save()

    class Meta:
        model = UserDocs
        fields = ['doc_title', 'doc_txt', 'doc_group']


class DocCreationFile(forms.ModelForm):
    """document creation from file"""
    doc_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('문서 제목 입력')}),
        label=_('문서 제목'),
        error_messages={
            'max_length': _('문서 제목의 최대 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)'),
        },
        help_text=_('제목란을 비워 둘 경우 "연번(책장별)/파일명/날짜"로 자동 설정됩니다.'),
        max_length=64,
        validators=[validators.MaxLengthValidator, ],
        required=False
    )
    doc_file = forms.FileField(
        label=_('파일 가져오기'),
        max_length=50,
        error_messages={
            'max_length': _('가져올 파일의 이름은 최대 %(max)d자 입니다. (현재 입력 %(length)d자)'),
        },
    )

    # choice field
    DEFAULT = 'DF'
    CASUAL = 'CA'
    NEWS = 'NA'
    LITERATURE = 'LI'
    ACADEMIC = 'AC'
    DOC_GROUP_CHOICES = [
        (DEFAULT, _('기본 책장')),
        (CASUAL, _('일상(SNS 등)')),
        (NEWS, _('뉴스기사')),
        (LITERATURE, _('문학')),
        (ACADEMIC, _('학술'))
    ]
    doc_group = forms.ChoiceField(
        choices=DOC_GROUP_CHOICES,
        label=_('보관할 책장 선택'),
        help_text=_('미선택시 기본 책장으로 자동 설정됩니다.'),
    )

    # def clean(self):
    #     cleaned_data = super().clean()

    class Meta:
        model = UserDocs
        fields = ['doc_title', 'doc_file', 'doc_group']


class DocCreationImage(forms.ModelForm):
    """document creation from image"""
    doc_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('문서 제목 입력')}),
        label=_('문서 제목'),
        error_messages={
            'max_length': _('문서 제목의 최대 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)'),
        },
        help_text=_('제목란을 비워 둘 경우 "연번(책장별)/파일명/날짜"로 자동 설정됩니다.'),
        max_length=64,
        validators=[validators.MaxLengthValidator, ],
        required=False
    )
    doc_img = forms.ImageField(
        label=_('이미지 가져오기'),
        max_length=50,
        error_messages={
            'max_length': _('가져올 이미지의 파일명은 최대 %(max)d자 입니다. (현재 입력 %(length)d자)'),
        },
    )

    # choice field
    DEFAULT = 'DF'
    CASUAL = 'CA'
    NEWS = 'NA'
    LITERATURE = 'LI'
    ACADEMIC = 'AC'
    DOC_GROUP_CHOICES = [
        (DEFAULT, _('기본 책장')),
        (CASUAL, _('일상(SNS 등)')),
        (NEWS, _('뉴스기사')),
        (LITERATURE, _('문학')),
        (ACADEMIC, _('학술'))
    ]
    doc_group = forms.ChoiceField(
        choices=DOC_GROUP_CHOICES,
        label=_('보관할 책장 선택'),
        help_text=_('미선택시 기본 책장으로 자동 설정됩니다.'),
    )

    # def clean(self):
    #     cleaned_data = super().clean()

    class Meta:
        model = UserDocs
        fields = ['doc_title', 'doc_img', 'doc_group']
