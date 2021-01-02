"""
Models Belongs to app2_user_settings
"""
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from app1_user_accounts.models import UserAccount


# Create your models here.


class LangSetting(models.Model):
    """User's Languages setting"""

    # a foreign key field from UserAccount
    user_id = models.ForeignKey(UserAccount,
                                on_delete=models.RESTRICT)

    # choice OPTIONS
    CHINESE = 'CN'
    KOREAN = 'KR'
    ENGLISH = 'EN'
    LANGUAGE_CHOICES = [
        (CHINESE, 'Chinese'),
        (KOREAN, 'Korean'),
        (ENGLISH, 'English'),
    ]
    # choice fields
    native_lang = models.CharField(
        max_length=2,
        verbose_name='native_lang',
        choices=LANGUAGE_CHOICES,
        default='native_lang'
    )
    target_lang1 = models.CharField(
        max_length=2,
        verbose_name='target_lang1',
        choices=LANGUAGE_CHOICES,
        default=CHINESE
    )
    target_lang2 = models.CharField(
        max_length=2,
        verbose_name='target_lang2',
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        null=True, blank=True
    )

    # datetime
    set_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='set_dt'
    )

    def __str__(self):
        return "<user no."+str(self.user_id)+"'s language setting>"

    class Meta:
        db_table = 'user_languages'
        verbose_name = 'User Language'
        verbose_name_plural = 'User Languages'


class AppSetting(models.Model):
    """User's App setting"""

    # a foreign key field from UserAccount
    user_id = models.ForeignKey(UserAccount,
                                on_delete=models.RESTRICT)

    # data fields
    # # choice field
    # DEFAULT = 'DF'
    # DARK_MODE = 'DK'
    # BRIGHT_MODE = 'BR'
    # SCREEN_CHOICES = [
    #     (DEFAULT, 'Default'),
    #     (DARK_MODE, 'Dark'),
    #     (BRIGHT_MODE, 'Light'),
    # ]
    # word_mark = models.CharField(
    #     max_length=1,
    #     verbose_name='word_mark',
    #     choices=WORD_MARK_CHOICES,
    #     default=VIEWED,
    # )
    screen_mode = models.CharField(
        max_length=32,
        verbose_name='screen_mode',
        default='default_theme'
    )
    txt_size = models.DecimalField(
        max_digits=3, decimal_places=1,
        validators=[MinValueValidator(7), MaxValueValidator(25)],
        verbose_name='text_size',
        default=12
    )
    dict_size = models.DecimalField(
        max_digits=3, decimal_places=1,
        validators=[MinValueValidator(7), MaxValueValidator(25)],
        verbose_name='dict_text_size',
        default=11
    )

    # boolean fields (agreements)
    notice_on = models.BooleanField(default=False)
    sms_agree = models.BooleanField(default=False)
    email_agree = models.BooleanField(default=False)

    # datetime
    set_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='setting modified at'
    )

    def __str__(self):
        return "<user no"+str(self.user_id)+"'s App setting>"

    class Meta:
        db_table = 'user_app_setting'
        verbose_name = 'User App Setting'
        verbose_name_plural = 'User App Settings'
