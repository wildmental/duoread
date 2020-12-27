"""forms for user accounts"""
from django import forms
from django.utils.timezone import datetime
from django.utils.translation import gettext as _

from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from app1_user_accounts.models import UserAccount


class LoginForm(forms.Form):
    """login form"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디(이메일 주소) 입력'}),
        error_messages={
            'required': '아이디는 필수 입력값입니다.',
            'max_length': '아이디 최대 길이는 %(limit_value)d자 입니다. (현재입력 %(show_value)d자)'
        },
        label='아이디',
        max_length=UserAccount._meta.get_field('username').max_length
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력'}),
        error_messages={
            'required': '비밀번호는 필수 입력값입니다.'
        },
        label='비밀번호'
    )

    class Meta:
        model = UserAccount
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user_account = UserAccount.objects.get(username=username)
            except UserAccount.DoesNotExist:
                self.add_error('username', "입력한 아이디가 존재하지 않습니다.")
                return
            if not check_password(password, user_account.password):
                self.add_error("password", '비밀번호가 틀립니다.')
            else:
                # temporary session code
                self.user_id = user_account.pk


class RegisterForm(UserCreationForm):
    """register form"""
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': _('이메일 주소는 로그인 아이디로 사용됩니다.')}),
        error_messages={
            'unique': _('이미 등록된 이메일 주소입니다. 비밀번호 찾기를 이용해 주세요.'),
            'required': _('이메일 주소는 필수 입력값입니다.'),
            'min_length': _('이메일 주소 최소 길이는 8자 입니다.'),
            'max_length': _('이메일 주소 최대 길이는 %s자 입니다.'
                            % (UserAccount._meta.get_field('username').max_length))
        },
        label=_('이메일*'),
        min_length=8,
        max_length=UserAccount._meta.get_field('username').max_length
    )
    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': _('사용자 이름 입력 (본명 또는 별명)')}),
        error_messages={
            'required': _('사용자 이름은 필수 입력값입니다.'),
            'min_length': _('사용자 이름 최소 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)'),
            'max_length': _('사용자 이름 최대 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)')
        },
        min_length=5,
        max_length=32,
        label=_('사용자 이름*')
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': _("비밀번호를 입력해주세요.")}
        ),
        error_messages={
            'required': _('비밀번호는 필수 입력값입니다.'),
            'min_length': _('비밀번호 최소 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)'),
            'max_length': _('비밀번호 최대 길이는 %(limit_value)d자 입니다. (현재 입력 %(show_value)d자)')
        },
        label='비밀번호*',
        min_length=8,
        max_length=32
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '비밀번호를 한번 더 입력해주세요'}
        ),
        error_messages={
            'required': '비밀번호 확인은 필수 입력값입니다.'
        },
        label='비밀번호 확인*'
    )
    birthdate = forms.DateField(
        widget=forms.DateInput(
            attrs={'placeholder': _('ex) 12/31/2020 = 2020년 12월 31일')}),
        label=_('생년월일'),
        required=False
    )

    class Meta:
        model = UserAccount
        fields = ['username', 'nickname', 'password', 'birthdate']
        field_classes = {'username': UsernameField}
        exclude = ('password',)

    def clean_password2(self):
        """have to check where does the ValidationError goes"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "비밀번호 확인을 정확히 입력해 주세요.")
        return password2


class UserChangeFrom(UserChangeForm):
    """user info change form"""

    class Meta:
        model = UserAccount
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def clean_password(self):
        print('[' + str(datetime.now()) + '] ' +
              '<UserAccount : %s> update' % self.initial.get('nickname'))
        return self.initial.get('password')
